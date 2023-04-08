import socket
import time

IP, PORT = ('127.0.0.1', 5006)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

n = time.time()

s.send(f"{n} - message 1".encode())

time.sleep(5)

s.send(f"{n} - message 2".encode())

s.close()