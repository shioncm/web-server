#import socket module
from socket import * 
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverport = 6789
serverSocket.bind(("", serverport))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() 
    print('Connected with ' + addr[0] + ':'
      + str(addr[1]))

    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.read()
 
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
        print('Success!')

        #Close client socket
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not found\r\n\r\n'.encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not found</h1></body></html>\r\n".encode())
        
        #Close client socket
        connectionSocket.close()
    except KeyboardInterrupt:
        print('Keyboard interrupt detected')
        connectionSocket.close()
        serverSocket.close()
        sys.exit()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
