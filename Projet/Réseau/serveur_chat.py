# Serveur chat UDP


import socket

BALISE_NEW_NAME = "__new_name__:"
BALISE_MESSAGE = "__message__:"
BALISE_QUIT = "__quit__"
IP, PORT = ('127.0.0.1', 5005)
adresses = {}


def send_entrance_notification(addr, name):
    """Gère l'arrivée de nouveau utilisateurs dans le chat
    
    Vérifie la validité du nom
    Ajoute le nom au dictionnaire des utilisateurs
    Prévient les utilisateurs déjà connectés de l'arrivée du nouvel utilisateur
    """

    # Si le nom demandé est déjà attribué
    if name in adresses.values():
        s.sendto("invalid_name".encode(), addr)     # On invalide le nom auprès du client

    # Si le nom demandé est valide
    else:
        s.sendto("valid_name".encode(), addr)  # On valide le nom auprès du client
        adresses[addr] = name   # Ajout du nom à la liste des utilisateurs

        
        # On prévient les utilisateurs déjà connectés de l'arrivée du nouvel utilisateur
        for key in adresses.keys():
            message_new_name = f"\n***{name}*** vient de rentrer dans le chat !\n"
            s.sendto(message_new_name.encode(), key)


def send_message(addr, message):
    """Gère l'envoi de messages

    Prévient les utilisateurs connectés de l'envoi d'un message
    """
    
    sender = adresses[addr]     # Auteur du message

    # Envoi du message à tous les utilisateurs connectés (sauf à l'auteur du message)
    for key in adresses.keys():
        if key != addr:
            message_sent = f"[{sender}] : {message}"
            s.sendto(message_sent.encode(), key)
    

def send_quit_notification(addr):
    """Gère la déconnexion d'un utilisateur

    Prévient les utilisateurs connectés de la déconnexion d'un utilisateur
    Envoie la balise de déconnexion à l'utilisateur qui a quitté le chat
    Supprime l'utilisateur du dictionnaire des utilisateurs
    """

    leaver = adresses[addr]     # Utilisateur qui quitte le chat

    # Envoi de la notification de déconnexion à tous les utilisateurs connectés (sauf à l'utilisateur qui quitte le chat)
    for key in adresses.keys():
        # Notification de déconnexion pour les utilisateurs connectés
        if key != addr:
            message_quit = f"***{leaver}*** a quitté le chat"
            s.sendto(message_quit.encode(), key)

        # Balise de déconnexion pour l'utilisateur qui quitte le chat
        else:
            s.sendto(BALISE_QUIT.encode(), key)
    
    del adresses[addr]  # Suppression de l'utilisateur du dictionnaire des utilisateurs
        

def traite_data(data, addr):
    """Traite les données reçues par le serveur

    Redirige les données vers les fonctions de traitement correspondantes
    """

    data = data.decode()
    
    # Entrée dans le chat
    if data.startswith(BALISE_NEW_NAME):
        name = data.split(BALISE_NEW_NAME)[1]
        send_entrance_notification(addr, name)
    
    # Envoi de messages
    elif data.startswith(BALISE_MESSAGE):
        message = data.split(BALISE_MESSAGE)[1]
        send_message(addr, message)
    
    # Déconnexion
    elif data.startswith(BALISE_QUIT):
        send_quit_notification(addr)

    # Requête inconnue
    else:
        print("Requête inconnue")


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP, PORT))

    while True:
        data, addr = s.recvfrom(1024)
        
        traite_data(data, addr)

    s.close()
