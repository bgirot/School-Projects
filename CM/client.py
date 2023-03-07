import socket
IP = '10.41.20.10'
PORT = 8080
MESSAGE = "hello world".encode()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((IP,PORT))
s.send(MESSAGE)

data = s.recv(1024)
print(data.decode())