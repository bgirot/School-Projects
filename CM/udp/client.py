import socket

IP = '127.0.0.1'
PORT = 5005
MESSAGE = "Let's go ça marche !".encode()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MESSAGE, (IP, PORT))