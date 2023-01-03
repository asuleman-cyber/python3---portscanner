# python3---portscanner

# Introduction
A Python port scanner is a program that uses the Python programming language to scan a network or host for open ports. Port scanning is a technique used to identify which network services, such as HTTP, FTP, and SSH, are running on a host and which ports they are using.  

To perform a port scan, the program will typically send a series of network packets to a range of predefined port numbers on the target host. If a port is open, the host will send a response back to the scanner indicating that the port is listening for connections. The scanner can then determine which ports are open and which services are running on those ports.  

In addition to identifying open ports, a Python port scanner may also provide additional information about the target host, such as the operating system and version, the type of hardware and software being used, and any vulnerabilities that may be present. This information can be useful for network administrators and security professionals who need to assess the security of a network or troubleshoot network issues.  

Overall, a Python port scanner is a useful tool for performing network reconnaissance and identifying potential security risks. 

# Code explanation 
This code prompts the user to enter an IP address and port range, then performs a port scan on the specified range in parallel using threading. The scan is divided into 5 threads, each of which scans a range of ports. This can make the scan faster, depending on the host and network.

The program also includes a scan() function that attempts to connect to a specific port and returns True if the connection is successful, and False if it is not.


