"""
    name: arp_monitor.py
    author: jessica soler
    date: 1/14/25
    purpose:
"""

from scapy.all import ARP, sniff
# sniffing packets on network
# ARP protocol
# scapy allows us to dissect packets and then put them back together

# who has? request
# who has this IP address and what is their MAC address?
def arp_display(pkt):
    # filter packets
    # if pkt is an arp packet
    # we only want this type of packet
    if pkt[ARP].op == 1:
        source_ip = pkt[ARP].psrc # p(packet)src(source)
        destination_ip = pkt[ARP].pdst # p(packet)dst(destination)
        
        return f"Request: {source_ip} is asking about {destination_ip}."
    
def main():
    sniff(
        # sniff has its own loop built into it, where it keeps sniffing over and over
        # each time it sniffs and finds something, we want it to display our arp_display function
        # keeps sniffing until program ends
        # don't want to caputer anything that isn't an ARP packet so we are filtering
        
        filter = "arp", # packet has been found-- takes only ARP packets
        prn = arp_display, # callback function, ARP packet filetered, dissect using scapy (prn means print?)
        store = 0,
        count = 20,        
    )


main()