# Python Networking Applications

Python networking projects completed through Western Nebraska Community College coursework, covering TCP sockets, threaded host discovery, and ARP packet monitoring.

## Projects

|Project|Description|Main concepts|
|-|-|-|
|[TCP client and server](tcp_client_server/README.md)|Send a message from a client to a listening server|IPv4 sockets, ports, UTF-8 encoding|
|[Command-line chat](tcp_chat/README.md)|Exchange messages between a client and server|Persistent connections, send/receive loops|
|[Threaded subnet scanner](subnet_scanner/README.md)|Find hosts that respond to ICMP ping|Subnets, threads, queues, locks, round-trip time|
|[ARP traffic monitor](arp_monitor/README.md)|Display ARP requests on a local network|Packet capture, filtering, callbacks|

## Setup

From the repository root in Windows PowerShell:

```powershell
py -3 -m venv .venv
.\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt
```

The TCP projects use Python's standard library. The scanner uses `pythonping`; the ARP monitor uses `scapy` and requires [Npcap](https://npcap.com/#download) on Windows. Run the scanner and ARP monitor from an Administrator PowerShell terminal.

Each project README includes run instructions and screenshots from local Windows demonstrations.

## Coursework credit

Completed by Jessica Soler through WNCC coursework using instructor-provided exercises and tutorials, including instruction by William Loring. 

## References

* [Python socket documentation](https://docs.python.org/3/library/socket.html)
* [Python threading documentation](https://docs.python.org/3/library/threading.html)
* [PythonPing](https://github.com/alessandromaggio/pythonping)
* [Scapy documentation](https://scapy.readthedocs.io/en/stable/)

