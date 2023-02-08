#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverport = 80
serversocket.bind((socket.gethostname(), serverport))
serversocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serversocket.accept() 
    
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = #Fill in start #Fill in end 
 
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end 
 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
 
        connectionSocket.close()
 
    except IOError:
        #Send response message for file not found
        #Fill in start 
        #Fill in end
        
        #Close client socket
        #Fill in start
        #Fill in end 

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
