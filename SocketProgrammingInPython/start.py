import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname('www.google.com')
print(ip)

#AF_INET : the address family ipv4
#SOCK_STREAM : connection oriented TCP protocol

