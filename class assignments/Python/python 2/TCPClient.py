#################################################################
#Name: Joshua Brack                                             #
#Date: 12/20/2020                                               #
#Class: CSC 450                                                 #
#Title: TCPClient                                               #
#Description: makes a request to server for a file              #
#Usage: python TCPClient.py server_ip server_port filename      #
#################################################################



from socket import *
import sys

#setup socket 
client_socket = socket(AF_INET, SOCK_STREAM)

#get values from cmd arguments
server_ip = str(sys.argv[1])
server_port = str(sys.argv[2])
filename = str(sys.argv[3])

#connect to server
client_socket.connect((server_ip, int(server_port)))

#Build GET request message
message = "GET /{} HTTP/1.1\r\nHost: {}\r\n".format(filename, server_ip)

print ("HTTP request to server:\r\n{}".format(message))

#make get request
client_socket.send(message.encode())

#recieve respone from server
response = client_socket.recv(2048)

print ("HTTP response from server:\r\n{}\n".format(response.decode()))

client_socket.close()
