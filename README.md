# Portscanner

# Introduction
Port scanning is a technique used to identify which network services, such as HTTP, FTP, and SSH, are running on a host and which ports they are using.  

To perform a port scan, the program will typically send a series of network packets to a range of predefined port numbers on the target host. If a port is open, the host will send a response back to the scanner indicating that the port is listening for connections. The scanner can then determine which ports are open and which services are running on those ports.  

In addition to identifying open ports, a Python port scanner may also provide additional information about the target host, such as the operating system and version, the type of hardware and software being used, and any vulnerabilities that may be present. This information can be useful for network administrators and security professionals who need to assess the security of a network or troubleshoot network issues.  

Overall, a Python port scanner is a useful tool for performing network reconnaissance and identifying potential security risks. 

# Code explanation 
This code prompts the user to enter an IP address and port range, then performs a port scan on the specified range in parallel using threading. The scan is divided into 5 threads, each of which scans a range of ports. This can make the scan faster, depending on the host and network.

The program also includes a scan() function that attempts to connect to a specific port and returns True if the connection is successful, and False if it is not.

# Screenshot
![image](https://github.com/asuleman-cyber/python3---portscanner/assets/43348989/b1bbe591-dfb0-456c-8494-b8ee90d5e3ea)

I ran a  test with my port scanner on my own machine, which is also known as "localhost" or 127.0.0.1. The goal was to see if there are any open ports on my machine within the range of 0 to 1000. Here's what I found:

- No open ports were found on 127.0.0.1 during the initial scan.
- However during subsequent scans ports 135 and 445 were open on my machine. These ports are commonly used for Windows RPC (Remote Procedure Call) and SMB (Server Message Block) services. Essentially It's like little doors that let different programs talk to each other.
- Additionally, port 3213 was found to be open on 127.0.0.1. The specific purpose and service associated with this port would need to be investigated further.
- No open ports were found on 127.0.0.1 in the subsequent scans.
