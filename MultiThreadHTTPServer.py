# Name: Tu Luong - 01649122
# Course: CIS 577
# Due Date: October 29, 2016
# Socket Programming Assignment 3: SMTP
# Professor: Paul Gracia

# import socket module
from socket import *
import threading


class UserThread(threading.Thread):

    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(1024)
                if not message:
                    break
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()

                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
                #Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i])
            except (IOError, IndexError):
                #Send response message for file not found
                connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><p>404 Not Found<p></body></html>")

serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
threads = []
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    print 'connected from', addr
    user_thread = UserThread(connectionSocket,addr)
    user_thread.setDaemon(True)
    user_thread.start()
    threads.append(user_thread)

serverSocket.close()
