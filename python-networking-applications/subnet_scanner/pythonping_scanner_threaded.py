"""
    pythonping_scanner_threaded.py
    jessica soler
    5/9/25
    This program promts the user to enter network address
    it uses pythonping library to detect active devices
    at each possible IP address in the range    
"""

import time
import threading
import queue
# https://docs.python.org/3/library/ipaddress.html
# convert ip/mask to list of hosts
import ipaddress
# Windows: pip install pythonping
# Linux Debian distributions:
#     sudo apt update
#     sudo apt install python3-pip
#     use sudo to run script: sudo python3 pythonping_scanner.py
from pythonping import ping

class PythonPingScanner():
    def __init__(self):
        # define a thread lock to prevent threads running into each other
        self.thread_lock = threading.Lock()
        
        # create thread queue to keep track of the threads
        self.q = queue.Queue()
        
        # simulates threads, you can increase or decrease this
        self.NUMBER_OF_THREADS = 254
        
        # initialize live hosts count
        self.hosts_count = 0
        
        print("+---------------------------------------------------+")
        print("|             Threaded Network Scanner              |")
        print("+---------------------------------------------------+")
        
        self.get_network_address()
        self.start_scan()
        
#---GET NETWORK ADDRESS--------------------------------------------------#
    def get_network_address(self):
        """get network address x.x.x.x/x or x.x.x.x/x.x.x.x from user"""
        #---FIND NETWORK ADDRESS------------------------------------------#
        # Use ipconfig in Windows, ifconfig in Linux
        # to find your local network address
        # Ex. If your IP address is 192.168.1.1
        # subnet mask: 255.255.255.0
        # Your network address is 192.168.1.0/24
        # If your subnet mask is different than 255.255.255.0
        # Type in the subnet mask directly: 192.168.10.0/255.255.255.252.0
        # 
        # change this to the default value of your network
        default_local_network = "10.0.1.0/24"
        
        # prompt the user to input a network address and press Enter
        # if they press enter without a network address, the default is used
        network_address = input("\nEnter your network address (ex. 192.168.1.0/24): ") or default_local_network
        
        print(f"Ping Scan: {network_address}")
              
        # create a netowrk address object from user input
        ip_net = ipaddress.ip_network(network_address)
        
        # convert ip_net ipaddress object into a list of all valid hosts
        self.all_hosts = list(ip_net.hosts())
        
        # for debugging
        # print(self.all_hosts)
        
#---SCAN NETWORK----------------------------------------------------#
    def start_scan(self):
        # store start time of program scan execution
        start_time = time.time()
        
        # create/spawn multiple threads
        for r in range(self.NUMBER_OF_THREADS):
            # set the thread target method
            thread = threading.Thread(target=self.worker)
            
            # all threads end when main program ends for cleaner shutdown
            thread.daemon = True
            
            # start/spawn the thread
            thread.start()
            
        # put all task requests in the queue
        for host in self.all_hosts:
            self.q.put(str(host))
            
        # block program from continuing
        # until all worker tasks are complete in the queue
        self.q.join()
        
        # calculate elapsed time for process
        scan_time = time.time() - start_time
        
        print(f"\nScan complete in {scan_time:.2f} seconds")
        print(f"Responding hosts: {self.hosts_count}")
            
#---THREAD WORKER----------------------------------------------------#
    def worker(self):
        while True:
            # get the next IP address from the queue
            host = self.q.get()
            
            # scan the IP address
            self.scan(host)
            
            # worker announces the task is done
            # task is removed from the queue
            self.q.task_done()

#---SCAN NETWORK----------------------------------------------------#
    def scan(self, ip):
        """Ping all IP addresses"""
        try:
            # ping the IP address with two packets
            result = ping(
                ip,         # target ip address 
                count=2,    # number of pings 
                timeout=2  # timeout in seconds
            )
            
            # if there was a successful ping
            if result.success():
                # thread_lock prevetns the threads from running into each other
                with self.thread_lock:
                    
                    # track count of live hosts
                    self.hosts_count += 1
                    
                    # response time less than 2000ms, target is active
                    print(f"{ip:14}--> RTT: {result.rtt_avg_ms:>6.2f} ms")
            
        except Exception as e:
            # catch the exception
            # print out the exception error for debugging
            print(f"Something went wrong: {e}")
            
            
#---MAIN PROGRAM----------------------------------------------------#
def main():
    # create program object to start program
    python_ping_scanner = PythonPingScanner()
    while True:
        menu = input("Another scan? (y/n): ").lower()
        if menu == "n":
            break
        python_ping_scanner.start_scan()
        
if __name__ == "__main__":
    main()