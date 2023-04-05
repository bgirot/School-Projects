import socket
import serveurHTTP

IP, PORT = ('127.0.0.1', 5006)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))

while True:
    s.listen()
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024)

        if not data:
            break

        print(data.decode())

    conn.close()

s.close()