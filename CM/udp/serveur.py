import socket

IP = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((IP,PORT))

data, addr = s.recvfrom(BUFFER_SIZE)

print("données reçues :", data.decode())

s.close()