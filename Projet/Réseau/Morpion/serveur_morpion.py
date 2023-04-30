## Jeu de morpion en réseau
## 
## Serveur

import socket
import random
import doctest



# Variables globales
JOIN_TAG = '__join__:'
QUIT_TAG = '__quit__'
PLAY_TAG = '__play__:'
IP, PORT = ('127.0.0.1', 5005)
players = {}     # sous la forme {<addr>:(<pseudo>, <valeur du symbole (1 ou 2)>, <symbole X ou O>)}
is_server_running = True
is_started_game = False
current_player = None



# Fonctions réseau
def player_arrival(data, addr):
    """Gère l'arrivée d'un joueur dans la partie

    
    Vérifie si la partie est pleine (2 joueurs max)
    Vérifie la validité du nom (s'il n'est pas déjà pris)
    Initialise la partie quand le nombre de joueurs (2) est suffisant

    Args:
        data (str): Le message envoyé par le joueur (de la forme "__join__:nom_du_joueur")
        addr (tuple): L'adresse du joueur
    """

    global is_started_game, players, current_player, board
    name = data.split(JOIN_TAG)[1]

    if len(players) >= 2:
        print("Third player tried to join, request denied")
        s.sendto("game_already_full".encode(), addr)

    else:
        if name in players.values():
            s.sendto("invalid_name".encode(), addr)
            print("Already existing name")
        else:
            s.sendto(name.encode(), addr)
            players[addr] = name

    # Si on a 2 joueurs, on lance la partie
    if len(players) == 2 and not is_started_game:
        print("Enough players, lets initalize the game")
        # On choisit aléatoirement le joueur qui commence
        current_player = random.choice(list(players.keys()))

        # On attribue les symboles X et O aux joueurs
        for address in players.keys():
            if address == current_player:
                players[address] = (players[address], 1, 'X')
            else:
                players[address] = (players[address], 2, 'O')

        # On crée le plateau de jeu
        board = generate_board(15,15)

        # On envoie le message de début de partie aux joueurs
        for address in players.keys():
            message = f"\n----------\nLa partie commence !\nVous avez le symbole {players[address][2]}\n{print_board(board)}\nC'est à *{players[current_player][0]}* de commencer\n"
            s.sendto(message.encode(), address)
        
        # La partie est lancée
        is_started_game = True
        print("Game initialized")


def end_game(reason, notable_addr):
    """Gère la fin de la partie

    Gère les 3 cas de fin de partie :
    - Un joueur quitte la partie
    - La partie est terminée (victoire ou égalité)
    - Le serveur est arrêté

    Args:
        reason (str): La raison de la fin de partie
        notable_addr (tuple): L'adresse du joueur qui a quitté la partie
                              si "player_left", l'adresse du gagnant si 
                              "game_done" et None si "server_stopped"
    """
    global players, is_server_running
    if reason == "player_left":
        leaver = players[notable_addr]

        for address in players:
            if address != notable_addr:
                message_quit = f"***{leaver}*** a quitté le jeu\nVous avez gagné par forfait (Appuyez sur Ctrl+C pour quitter)"
                s.sendto(message_quit.encode(), address)
            else:
                message_quit = f"Vous avez quitté le jeu\nVous avez donc perdu par forfait (Appuyez sur Ctrl+C pour quitters)"
                s.sendto(message_quit.encode(), address)

            s.sendto(QUIT_TAG.encode(), address)

    elif reason == "game_done":
        for address in players:
            if address != notable_addr:
                message_quit = f"La partie est terminée\nVous avez perdu (Appuyez sur Ctrl+C pour quitter)"
                s.sendto(message_quit.encode(), address)
            else:
                message_quit = f"La partie est terminée\nVous avez gagné (Appuyez sur Ctrl+C pour quitter)"
                s.sendto(message_quit.encode(), address)
    
    else:
        for address in players:
            message_quit = f"Le serveur a été arrêté\nNous vous prions de nous excuser pour la gêne occasionnée\nVous pouvez quitter le jeu (Appuyez sur Ctrl+C pour quitter)"
            s.sendto(message_quit.encode(), address)
    
    # On arrête le serveur
    players = {}
    is_server_running = False


def player_move_handler(move, addr):
    """Gère les coups joués par les joueurs

    Vérifie que la partie a bien commencé (les 2 joueurs sont présents)
    Vérifie que c'est bien au tour du joueur qui a joué
    Joue le coup

    Args:
        data (str): Le message envoyé par le joueur (de la forme "__play__:coup_joué")
        addr (tuple): L'adresse du joueur ayant joué
    """
    global current_player, players, is_started_game, board

    # On vérifie que la partie a commencé
    if not is_started_game:
        print("Game not started and player tried to play")
        message = f"La partie n'a pas commencé ({len(players)}/2 joueurs), veuillez attendre"
        s.sendto(message.encode(), addr)

    # On vérifie ensuite que c'est bien au tour du joueur qui a joué
    elif addr != current_player:
        print("Player tried to play but it's not his turn")
        message = f"Ce n'est pas à vous de jouer"
        s.sendto(message.encode(), addr)
    
    # Si tout est bon, on joue le coup (qui n'est pas forécément valide mais ça sera vérifié par les fonctions du jeu)
    else:
        print(f"Legit move : {move}, now we play it on the server")

        # On commence à jouer le coup
        # Si le coup est jouable
        if can_play(board, move):
            board = play_move(board, move, players[addr][1])
            print(board)

            for address in players.keys():
                # On envoie le plateau de jeu mis à jour aux joueurs
                message = f"\n*{players[current_player][0]}* a joué en {move}\n{print_board(board)}"
                s.sendto(message.encode(), address)
            
            # On vérifie si le coup joué est gagnant
            if check_win(board, players[addr][1]):
                print("Game done")
                end_game("game_done", addr)
            
            # On vérifie si le coup joué est un match nul
            elif check_draw(board):
                print("Game done")
                end_game("game_done", None)
            
            # Si le coup n'est ni gagnant ni un match nul, on passe au joueur suivant
            else:
                if current_player == list(players.keys())[0]:
                    current_player = list(players.keys())[1]
                    print(f"Next player : {current_player}")
                else:
                    current_player = list(players.keys())[0]
                    print(f"Next player : {current_player}")
                
                for address in players.keys():
                    s.sendto(f"C'est à *{players[current_player][0]}* de jouer\n".encode(), address)
        
        # Si le coup n'est pas jouable
        else:
            print("Move not legit")
            message = f"Coupe invalide ! Veuillez rejouer"
            s.sendto(message.encode(), addr)
                
        
def process_data(data, addr):
    """Traite les données reçues par le serveur

    Vérifie la nature des données reçues et appelle la fonction adéquate

    Args:
        data (str): Les données reçues
        addr (tuple): L'adresse de l'expéditeur
    """
    print(data)
    if data.startswith(JOIN_TAG):
        player_arrival(data, addr)

    elif data.startswith(PLAY_TAG):
        data = data.split(PLAY_TAG)[1]
        player_move_handler(data, addr)

    elif data == QUIT_TAG:
        end_game("player_left", addr)

    else:
        print("Unknown data received")
    


# Fonctions du jeu
def generate_board(row, col):
    """Génère un plateau de jeu vide

    Args:
        row (int): Le nombre de lignes du plateau
        col (int): Le nombre de colonnes du plateau

    Returns:
        list: Le plateau de jeu vide pleine de 0
    """

    return [[0 for x in range(col)] for y in range(row)]


def print_board(board):
    """Affiche le plateau de jeu

    La fonction affiche le plateau de jeu en fonction de sa taille
    La limite est 26 colonnes (A-Z) et 999 lignes (0-999)

    Args:
        board (list): Le plateau de jeu

    Returns:
        str: Le plateau de jeu affiché
    """

    display_board = ""

    row_nbr_width = 0
    if len(board) < 10:
        row_nbr_width = 1
    elif len(board) >= 10 and len(board) <= 100:
        row_nbr_width = 2
    else:
        row_nbr_width = 3

    # Footer
    footer = ""
    alphabet = [chr(i) for i in range(65, 91)]
    footer += " " * (row_nbr_width + 1)
    for i in range(len(board[0])):
        footer += "--"
    footer += f"\n{row_nbr_width * ' '} "
    for i in range(len(board[0])):
        footer += f" {alphabet[i]}"
    
    # Affichage ligne par ligne
    for i in range(len(board)):
        current_line = f"{i}|"
        while len(current_line) < row_nbr_width + 1:
            current_line = " " + current_line
        table = str.maketrans("012", ".XO")
        for elem in board[i]:
            current_line += " " + str(elem).translate(table)
        display_board += current_line + "\n"
    display_board += footer
    return display_board


def can_play(board, move):
    """Vérifie si le coup joué est possible

    Args:
        board (list): Le plateau de jeu
        player (int): Le joueur
    
    Returns:
        bool: True si le joueur peut jouer, False sinon
    """
    
    possible_row = [str(i) for i in range(len(board))]
    possible_col = [chr(i + 65) for i in range(len(board[0]))]

    if move[0] in possible_col and move[1:] in possible_row:
        x = ord(move[0]) - 65
        y = int(move[1:])
        if board[y][x] == 0:
            return True
    return False


def play_move(board, move, player):
    """Joue un coup sur le plateau de jeu

    Le coup doit être valide, c'est-à-dire qu'il doit être possible de jouer ce coup

    Args:
        board (list): Le plateau de jeu
        move (str): Le coup à jouer
        player (int): Le pion du joueur

    Returns:
        board (list): Le plateau de jeu modifié par le coup
    """

    move = (ord(move[0]) - 65, int(move[1:]))
    board[move[1]][move[0]] = player
    return board


def check_vertical_win(board, player):
    """Vérifie si le joueur a gagné verticalement (5 pions alignés)
    
    Args:
        board (list): Le plateau de jeu
        player (int): Le pion du joueur
    
    Returns:
        bool: True si le joueur a gagné verticalement, False sinon
    
    >>> check_vertical_win([[1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 2, 0, 0, 0]], 1)
    True
    >>> check_vertical_win([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 2, 0, 0, 0], [1, 0, 0, 0, 0], [1, 2, 0, 0, 0]], 1)
    False
    """

    for col in range(len(board)):
        counter = 0
        for row in board:
            if row[col] == player:
                counter += 1
            else:
                counter = 0
            if counter == 5:
                return True
    return False


def check_horizontal_win(board, player):
    """Vérifie si le joueur a gagné horizontalement (5 pions alignés)
    
    Args:
        board (list): Le plateau de jeu
        player (int): Le pion du joueur
    
    Returns:
        bool: True si le joueur a gagné horizontalement, False sinon

    >>> check_horizontal_win([[1, 1, 1, 1, 1], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [0, 0, 0, 2, 2]], 1)
    True
    >>> check_horizontal_win([[1, 1, 1, 2, 1], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [0, 0, 0, 0, 2], [2, 0, 0, 2, 2]], 1)
    False
    """

    for row in board:
        counter = 0
        for item in row:
            if item == player:
                counter += 1
            else:
                counter = 0
            if counter == 5:
                return True
    return False


def check_rising_diagonal_win(board, player):
    """ Vérifie si le joueur a gagné en verticale montante (5 pions alignés)
    
    Par diagonale montante, on entend une diagonale qui va du bas-gauche vers le haut-droite
    selon l'affichage du plateau de jeu et non selon la représentation matricielle

    Args:
        board (list): Le plateau de jeu
        player (int): Le pion du joueur
    
    Returns:
        bool: True si le joueur a gagné en verticale montante, False sinon

    >>> check_rising_diagonal_win([[1, 0, 0, 0, 2], [2, 1, 0, 2, 0], [2, 2, 2, 0, 0], [2, 2, 2, 1, 0], [2, 2, 2, 2, 1]], 2)
    True
    >>> check_rising_diagonal_win([[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [2, 0, 1, 0, 0], [2, 2, 0, 1, 0], [2, 2, 2, 0, 2]], 1)
    False
    """

    if len(board[0]) < 5 or len(board) < 5:
        return False
    
    for row in range(4, len(board)):
        for col in range(len(board[0])-4):
            if board[row][col] == player:
                if board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == board[row-4][col+4] == player:
                    return True
    return False


def check_falling_diagonal_win(board, player):
    """Vérifie si le joueur a gagné en verticale descendante (5 pions alignés)

    Par diagonale descendante, on entend une diagonale qui va du haut-gauche vers le bas-droite
    selon l'affichage du plateau de jeu et non selon la représentation matricielle

    Args:
        board (list): Le plateau de jeu
        player (int): Le pion du joueur

    Returns:
        bool: True si le joueur a gagné en verticale descendante, False sinon

    >>> check_falling_diagonal_win([[1, 0, 0, 0, 2], [2, 1, 0, 2, 0], [2, 2, 1, 0, 0], [2, 2, 2, 1, 0], [2, 2, 2, 2, 1]], 1)
    True
    >>> check_falling_diagonal_win([[2, 0, 0, 0, 0], [0, 1, 0, 0, 0], [2, 0, 1, 0, 0], [2, 2, 0, 1, 0], [2, 2, 2, 0, 2]], 1)
    False
    """

    if len(board[0]) < 5 or len(board) < 5:
        return False

    for row in range(len(board)-4):
        for col in range(len(board[0])-4):
            if board[row][col] == player:
                if board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == board[row+4][col+4]== player:
                    return True
    return False


def check_win(board, player):
    """Vérifie si le joueur a gagné (5 pions alignés)

    Compilé les fonctions check_vertical_win, check_horizontal_win, check_rising_diagonal_win et check_falling_diagonal_win

    Args:
        board (list): Le plateau de jeu
        player (int): Le pion du joueur
    
    Returns:
        bool: True si le joueur a gagné, False sinon
    """

    if check_vertical_win(board, player) or check_horizontal_win(board, player) or check_rising_diagonal_win(board, player) or check_falling_diagonal_win(board, player):
        return True
    return False


def check_draw(board):
    """Vérifie si le plateau est plein
    
    Args:
        board (list): Le plateau de jeu
    
    Returns:
        bool: True si le plateau est plein, False sinon
    """

    for row in board:
        if 0 in row:
            return False
    return True



# Main
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((IP, PORT))

    while True:
        if not is_server_running:
            break

        data, addr = s.recvfrom(1024)

        process_data(data.decode(), addr)
