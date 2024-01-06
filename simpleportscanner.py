from socket import *

ip_address = input("Enter IP address: ")
port_start = int(input("Enter starting port number: "))
port_end = int(input("Enter ending port number: "))

print(f"Scanning ip: {ip_address}")
for port in range(port_start, port_end + 1):
    print(f"Scanning port {port} ... ")
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(5)
    if (s.connect_ex((ip_address, port)) == 0):
        print(f"Port {port} is open")

    s.close()

print("Finished Scanning!")