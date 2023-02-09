## importing socket module
import socket
## getting the hostname by socket.gethostname() method
ip_address = socket.gethostbyname(socket.gethostname())
print(f"IP Address: {ip_address}") #127.0.1.1