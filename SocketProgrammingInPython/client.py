#import socket module
import socket

#Create a socket object
s = socket.socket()

#Define the port on which you to connect
port = 12345
#connect to the server on local computer
s.connect(('127.0.0.1',port))

#receive data from the server
print ((s.recv(1024)).decode()) # byte를 정해준 것. string을 받겠다! 이렇게.
#close the connection
s.close()