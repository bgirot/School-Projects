import socket, threading

IP, PORT = ('127.0.0.1', 5006)

def handle(conn):

    while True:
        data = conn.recv(1024)

        if not data:
            break

        print(data.decode())

    conn.close()


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, PORT))
    s.listen()

    while True:

        conn, addr = s.accept()

        threading.Thread(target=handle, args=[conn]).start()
    
    s.close()