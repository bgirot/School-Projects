import socket
import time

IP, PORT = ('127.0.0.1', 5006)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

s.send("Message n°1 : OK".encode())

time.sleep(2)

s.send("Message n°2 : OK".encode())

s.close()