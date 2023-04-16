## Client chat UDP

import socket, threading, doctest

BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"
IP, PORT = ('127.0.0.1', 5005)


def new_user_handler():
    """Gère l'arrivée de l'utilisateur dans le chat

    Vérifie la validité du nom en fonction de la réponse du serveur
    """

    # Demande du nom de l'utilisateur jusqu'à ce qu'il soit valide
    while True:
        name = input("Enter your name : ")
        name = BALISE_NEW_NAME+name
        s.sendto(name.encode(), (IP, PORT))
        
        # On attend la réponse du serveur sur la validité du nom
        data, addr = s.recvfrom(1024)

        # Si le nom est valide, on sort de la boucle
        if data.decode() == "valid_name":
            break
        # Sinon, on redemande un nom
        else:
            print("Le nom entré est déjà attribué")


def send():
    """Gère l'envoi de messages

    Envoie le message au serveur
    Envoie la balise de déconnexion au serveur si la commande "quit" est entrée
    """

    while True:
        message = input()

        # Si la commande "quit" est entrée, on envoie la balise de déconnexion
        if message == "quit":
            s.sendto(BALISE_QUIT.encode(), (IP, PORT))

            # On ferme le thread d'envoi (on ferma le socket plus tard dans receive)
            break

        # Sinon, on envoie le message de l'utilisateur
        else:
            message = BALISE_MESSAGE+message
            s.sendto(message.encode(), (IP, PORT))


def receive():
    """Gère la réception de données du serveur

    Affiche les données reçues du serveur
    """

    while True:
        data, addr = s.recvfrom(1024)

        # Si le serveur nous déconnecte (du normalement à la demande de déconnexion effectuée par le thread d'envoie)
        if data.decode() == BALISE_QUIT:
            # On ferme le socket puis le thread
            s.close()
            break

        # Sinon on affiche les données (messages) reçus du serveur
        else:
            print(data.decode())


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Arrivée dans le chat
    new_user_handler()

    # Envoi
    threading.Thread(target=send).start()

    # Réception
    threading.Thread(target=receive).start()
