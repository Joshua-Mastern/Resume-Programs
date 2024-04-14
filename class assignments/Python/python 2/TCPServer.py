#################################################################
#Name: Joshua Brack                                             #
#Date: 12/20/2020                                               #
#Class: CSC 450                                                 #
#Title: TCPServer                                               #
#Description: recieves request from client and responds         #
#Usage: python TCPServer.py                                     #
#################################################################



from socket import *

#SETUP SOCKET
server_socket = socket(AF_INET, SOCK_STREAM)

#client can have any ip address and connects through port
server_socket.bind(('',12000))

#start listening
server_socket.listen(1)

print("The server is ready to recieve...\n")


connection_socket, address = server_socket.accept()

request_message = connection_socket.recv(2048)

#http request
print("HTTP request:\r\n{}".format(request_message.decode()))
#object to be fetched
words = request_message.decode().split()
theObject = words[1][1:]
print("Object to be fetched: {}".format(theObject))
#Response message - search for object
        #if object exists
                #200 ok
                #body of data
        #else
                #404 Not Found

try:
        f=open(theObject)
        print("Object Content:\n{}\n".format(f.read()))
        f.seek(0)
        response_message = "HTTP/1.1 200 OK\n\n{}".format(f.read())
        f.seek(0)
except:
        response_message = "HTTP/1.1 404 Not Found"

#print response message
print("HTTP response message:\n{}\n".format(response_message))
#send response message
connection_socket.send(response_message.encode())

server_socket.close()
