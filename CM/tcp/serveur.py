import socket

IP = '127.0.0.1'
PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen()


while True:
    s_connection, addr = s.accept()

    while True:
        data = s_connection.recv(BUFFER_SIZE)
        if not data:
            break
        print(data.decode())

s_connection.close()

s.close()