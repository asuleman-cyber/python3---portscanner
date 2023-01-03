import socket
import threading

def scan(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
        return True
    except:
        return False

def start_scan(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        if scan(host, port):
            open_ports.append(port)
    return open_ports

def scan_thread(host, start_port, end_port):
    open_ports = start_scan(host, start_port, end_port)
    if open_ports:
        print(f"Ports {', '.join([str(p) for p in open_ports])} are open on {host}")
    else:
        print(f"No open ports found on {host}")

def main():
    host = input("Enter the IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    print(f"Scanning {host} for open ports...")

    t1 = threading.Thread(target=scan_thread, args=(host, 1, 1024))
    t2 = threading.Thread(target=scan_thread, args=(host, 1024, 2048))
    t3 = threading.Thread(target=scan_thread, args=(host, 2048, 3072))
    t4 = threading.Thread(target=scan_thread, args=(host, 3072, 4096))
    t5 = threading.Thread(target=scan_thread, args=(host, 4096, end_port))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

if __name__ == '__main__':
    main()
