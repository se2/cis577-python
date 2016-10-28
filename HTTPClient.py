# Name: Tu Luong - 01649122
# Course: CIS 577
# Due Date: October 29, 2016
# Socket Programming Assignment 3: SMTP
# Professor: Paul Gracia

from socket import *
import sys

try:

	server_address = sys.argv[1]
	server_port = int(sys.argv[2])
	filename = sys.argv[3]

	server_host = "%s:%s" %(server_address, server_port)

except IndexError:
	print "missing arguments"
	sys.exit(1)

try:

	client_socket = socket(AF_INET,SOCK_STREAM)

	client_socket.connect((server_address, server_port))

	header = {
		"Header" : "GET /%s HTTP/1.1" %(filename),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-us",
		"Host": server_host,
	}

	http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)

	# print http_header
	client_socket.send("%s\r\n\r\n" %(http_header))

except IOError:
	print "file not found"
	sys.exit(1)

final_msg = ""

response_msg = client_socket.recv(1024)

while response_msg:
	final_msg += response_msg
	response_msg = client_socket.recv(1024)

client_socket.close()

print final_msg
