## importing socket module
import socket
## getting the hostname by socket.gethostname() method
ip_address = socket.gethostbyname("localhost")
print(f"IP Address: {ip_address}") #127.0.1.1

host = socket.gethostname()
print(f"IP Address 2: {host}")

ip2 = socket.gethostbyname(socket.gethostname())
print(f"IP Address 3: {ip2}")
