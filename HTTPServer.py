# Name: Tu Luong - 01649122
# Course: CIS 577
# Due Date: October 29, 2016
# Socket Programming Assignment 3: SMTP
# Professor: Paul Gracia

#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a server socket
serverSocket.bind(('', 8080))
serverSocket.listen(1)

while True:

    #Establish the connection
    print 'Ready to serve...'
    connectionSocket,addr =  serverSocket.accept()
    print 'connected from', addr
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print filename
        f = open(filename[1:])
        outputdata = f.read()

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')

        #Send the content of the requested file to the client
        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except (IOError, IndexError) as e:
        print e
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
	connectionSocket.send('404 File Not Found')
        #Close Client socket
        connectionSocket.close()

serverSocket.close()
