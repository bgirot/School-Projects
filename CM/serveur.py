import socket
IP = '10.41.20.10'
PORT = 8080
BUFFER_SIZE= 1024       # On pourrait mettre 2^16 pour plus de données (max accepté par IP)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP,PORT))
s.listen()

s_connexion, addr = s.accept()

data = s_connexion.recv(BUFFER_SIZE)
print(data.decode())
MESSAGE_RECEPT = "received data : " + data.decode()
s_connexion.send(MESSAGE_RECEPT.encode())

s_connexion.close()
s.close()