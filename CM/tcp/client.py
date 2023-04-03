import socket
import time

IP = '127.0.0.1'
PORT = 5005
request1 = "get /index1.html HTTP/1.0\r\n\r\n".encode()      # Requête HTTP
request2 = "get /index2.html HTTP/1.1\r\n\r\n".encode()     # Requête HTTP
request3 = "get /index3.html HTTP/1.1\r\n\r\n".encode()     # Requête HTTP
request_list = [request1, request2, request3]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Ouvre un socket en IPv4 (AF_INET) en TCP (SOCK_STREAM) car TCP nécessaire pour HTML
s.connect((IP, PORT))

for req in request_list:
    s.send(req)
    time.sleep(1)

s.close()