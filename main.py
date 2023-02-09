#import socket module
from socket import * 
# import socket
import sys # In order to terminate the program

# print(socket.gethostbyname(socket.gethostname()))

serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Prepare a sever socket
serverport = 6787
serverSocket.bind(('', serverport))
serverSocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    
    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1] 
        print(filename + '\n')
        f = open(filename[1:]) 
        outputdata = f.read()
 
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
        print('Success!')

        #Close client socket
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not found\r\n\r\n')
        connectionSocket.send("<html><head></head><body><h1>404 Not found</h1></body></html>\r\n")
        
        #Close client socket
        connectionSocket.close()
    except KeyboardInterrupt:
        print('Keyboard interrupt detected')
        connectionSocket.close()
        serverSocket.close()
        sys.exit()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
