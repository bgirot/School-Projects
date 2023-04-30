## Jeu de morpion en réseau
##
## Client

import socket, threading


# Variables globales
JOIN_TAG = '__join__:'
QUIT_TAG = '__quit__'
PLAY_TAG = '__play__:'
IP, PORT = ('127.0.0.1', 5005)
is_game_starting = True


# Fonctions réseau
def new_user_handler():
    global is_game_starting
    while True:
        name = JOIN_TAG + input("Enter your name : ")
        s.sendto(name.encode(), (IP, PORT))

        # On attend la validation du serv
        data, addr = s.recvfrom(1024)
        server_name_response = data.decode()

        # Si le serv prévient que la game est full
        if server_name_response == "game_already_full":
            print("La partie est déjà pleine, essayez de vous connecter plus tard")
            is_game_starting = False
            break
        
        # Si le nom est déjà attribué
        elif server_name_response == "invalid_name":
            print("Le nom a déjà été attribué, entrez un nouveau nom")
        
        # Si tout va bien (la réponse serveur correspond au pseudo accepté)
        else:
            print(f"Bienvenue {server_name_response} !")
            break

def sender():
    while True:
        message = input()

        if message == "quit":
            s.sendto(QUIT_TAG.encode(), (IP, PORT))
        
        else:
            message = PLAY_TAG + message
            s.sendto(message.encode(), (IP, PORT))


def receiver():
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode()

        # Quand le serv arrête le jeu
        if data == QUIT_TAG:
            break

        else:
            print(data)


# Main
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    new_user_handler()

    if is_game_starting:
        threading.Thread(target=sender).start()
        threading.Thread(target=receiver).start()
    