import doctest

def generer_grille_vide(nb_col,nb_lig) :
    """
        Étant donnés un nombre de colonnes et un nombre de ligne, retourne une grille vide de telles dimensions
        sous forme de liste
        Les cases vides sont représentées par des zéros
        
        :param nb_col: Nombre de colonnes
        :param nb_lig: Nombre de lignes
        :type nb_col: int
        :type nb_lig: int
        :return: Grille vide sous forme de liste
        :rtype: list

        .. note:: cette fonction s'assure que la grille a des dimension positives et existe (au moins 1 col ou une ligne)

        :Example:

        >>> generer_grille_vide(7,6)
        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        >>> generer_grille_vide(1,3)
        [[0], [0], [0]]
    """
    # Assertion de l'existence de la grille
    assert nb_col > 0 and nb_lig > 0, "unsupported dimensions"

    # Génération de la grille
    return [[0 for x in range(nb_col)] for y in range(nb_lig)]

def affiche_grille(grille) :
    """
        Étant donné une grille en argument, affiche cette grille en représentant les pions du joueur 1 par des X,
        ceux du joueur 2 par des O et les cases vides par des espaces

        :param grille: grille à afficher
        :type grille: list
        :return: affichage de la grille
        :rtype: NoneType

        .. note:: cette fonction ne retourne rien, mais affiche quelque chose avec print()

        :Example:

        >>> affiche_grille([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]])
        +-+-+-+-+-+-+-+
        | | | | | | | |
        +-+-+-+-+-+-+-+
        | |X|O|X| | | |
        +-+-+-+-+-+-+-+
        | |X|O|O| | | |
        +-+-+-+-+-+-+-+
        | |O|X|X| |X|O|
        +-+-+-+-+-+-+-+
        |O|X|O|O|X|O|O|
        +-+-+-+-+-+-+-+
        |X|X|O|X|O|X|X|
        +-+-+-+-+-+-+-+
         0 1 2 3 4 5 6
    """
    # Line divider
    line_divider = "+"
    for i in range(len(grille[0])):
        line_divider += "-+"

    # Footer
    footer = ""
    for i in range(len(grille[0])):
        footer += f" {i}"

    # Display
    for line in reversed(grille):
        # Ligne courante à afficher
        current_line = "|"
        # Remplace 0, 1, 2 respectivement par espace, X, O
        table = str.maketrans("012"," XO")                      # Table de traduction
        for elem in line:
            current_line += str(elem).translate(table) + "|"    # Remplacement grâce à la table de traduction
        print(line_divider)
        print(current_line)
    print(line_divider)
    print(footer)

def peut_jouer(grille,colonne) :
    """
        Étant donné une grille et une colonne dans laquelle le joueur veut jouer, retourne True s'il est
        possible de jouer dans cette colonne, sinon False

        :param grille: Grille courante
        :param colonne: Colonne dans laquelle le joueur veut jouer
        :type grille: list
        :type colonne: int
        :return: Est-il possible de jouer dans cette colonne ?
        :rtype: bool

        :Example:

        >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],3)
        True
        >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,1,0,0,0,0,0]],1)
        False
        >>> peut_jouer([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],99)
        False
    """
    # Si la grille donnée n'existe pas
    if colonne >= len(grille[0]) or colonne < 0:
        return False

    # Peut-on jouer dans cette colonne ?
    return grille[-1][colonne] == 0

def joue(grille,colonne,joueur) :
    """
        Étant donné une grille, un joueur courante et une colonne dans laquelle il joue (en considérant l'action
        jouable), retourne la grille une fois que le joueur a joué
        
        :param grille: grille courante
        :param colonne: colonne dans laquelle le joueur joue
        :param joueur: joueur courant
        :type grille: list
        :type colonne: int
        :type joueur: int
        :return: la grille une fois que le joueur a joué
        :rtype: list

        :Example:

        >>> joue([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],0,1)
        [[1, 1, 2, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [1, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        >>> joue([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2,2)
        [[1, 1, 2, 1, 2, 1, 1], [2, 1, 2, 2, 1, 2, 2], [0, 2, 1, 1, 0, 1, 2], [0, 1, 2, 2, 0, 0, 0], [0, 1, 2, 1, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0]]
    """
    # Trouver la position de la case à mettre à jour puis mettre la grille à jour
    for i in range(len(grille)):
        if grille[i][colonne] == 0:
            grille[i][colonne] = joueur
            break
    return grille

def a_gagne_vert(grille,joueur) :
    """
        Étant donné une grille et un joueur, retourne True si ce joueur a gagné verticalement

        :param grille: grille à tester
        :param joueur: joueur dont la victoire doit être vérifiée
        :type grille: list
        :type joueur: int
        :return: ce joueur a-t-il gagné verticalement ?
        :rtype: bool

        .. seealso:: a_gagne_hor(grille,joueur), a_gagne_diag1(grille,joueur), a_gagne_diag2(grille,joueur)

        :Example:

        >>> a_gagne_vert([[1,1,2,1,2,1,1],[2,1,2,2,1,2,1],[0,2,1,1,0,1,1],[0,1,2,2,0,0,1],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        True
        >>> a_gagne_vert([[1,1,2,1,2,1,1],[2,1,2,2,1,2,1],[0,2,2,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        True
        >>> a_gagne_vert([[1,1,2,1,2,1,1],[2,1,2,2,1,2,1],[0,2,1,1,0,1,2],[0,1,2,2,0,0,2],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        False
    """
    for column in range(len(grille[0])):
        # On définit un compteur pour suivre la streak du joueur
        counter = 0
        for line in grille:
            if line[column] == joueur:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
    return False

def a_gagne_hor(grille,joueur) :
    """
        Étant donné une grille et un joueur, retourne True si ce joueur a gagné horizontalement

        :param grille: grille à tester
        :param joueur: joueur dont la victoire est à tester
        :type grille: list
        :type joueur: int
        :return: ce joueur a-t-il gagné horizontalement ?
        :rtype: bool

        .. seealso:: a_gagne_vert(grille,joueur), a_gagne_diag1(grille,joueur), a_gagne_diag2(grille,joueur)

        :Example:

        >>> a_gagne_hor([[1,1,1,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        True
        >>> a_gagne_hor([[1,1,2,1,2,1,1],[2,1,1,2,2,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        True
        >>> a_gagne_hor([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        False
    """
    for line in grille:
        # Même méthode que pour a_gagne_vert()
        counter = 0
        for i in range(len(grille[0])):
            if line[i] == joueur:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
    return False
            
def a_gagne_diag1(grille,joueur) :
    """
        Étant donné une grille et un joueur, retourne True si ce joueur a gagné en diagonale montante

        :param grille: grille à tester
        :param joueur: joueur dont la victoire est à vérifier
        :type grille: list
        :type joueur: int
        :return: ce joueur a-t-il gagné en diagonale montante ?
        :rtype: bool

        .. seealso:: a_gagne_vert(grille,joueur), a_gagne_hor(grille,joueur), a_gagne_diag2(grille,joueur)
        .. note:: cette méthode ne fonctionne que dans des grille de valeur supérieure à 4x4 (même si évidemment une diagonale
                  de 4 n'existe pas dans une grille de telles dimensions), donc on ajoute une simplement une condition sur la 
                  taille de la grille

        :Example:

        >>> a_gagne_diag1([[1,2,1,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,1,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        True
        >>> a_gagne_diag1([[1,1,2,2,2,1,1],[2,1,1,2,2,1,2],[0,2,1,1,0,2,2],[0,1,2,2,0,0,2],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        True
        >>> a_gagne_diag1([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        False
    """
    # Retourne automatiquement False si les dimensions de la grille sont inférieures à 4x4 pcq il n'y a pas de diagonales dans une grille de telles dimensions
    if len(grille[0]) < 4 or len(grille) < 4:
        return False
    
    # Chaque fois qu'on voit un pion du joueur on teste sa diagonale montante
    for line in range(len(grille)-3):               # On réduit la grille de recherche aux départs possibles de diagonales
        for column in range(len(grille[0])-3):      # Idem
            if grille[line][column] == joueur:
                if grille[line+1][column+1] == grille[line+2][column+2] == grille[line+3][column+3] == joueur:
                    return True
    return False

def a_gagne_diag2(grille,joueur) :
    """
        Étant donné une grille et un joueur, retourne True si ce joueur a gagné en diagonale descendante

        :param grille: grille à tester
        :param joueur: joueur dont la victoire est à vérifier
        :type grille: list
        :type joueur: int
        :return: ce joueur a-t-il gagné en diagonale descendante ?
        :rtype: bool

        .. seealso:: a_gagne_vert(grille,joueur), a_gagne_hor(grille,joueur), a_gagne_diag2(grille,joueur)
        .. note:: cette méthode ne fonctionne que dans des grille de valeur supérieure à 4x4 (même si évidemment une diagonale
                  de 4 n'existe pas dans une grille de telles dimensions), donc on ajoute une simplement une condition sur la 
                  taille de la grille

        :Example:

        >>> a_gagne_diag2([[1,1,2,1,2,1,1],[2,1,1,2,1,2,2],[2,1,1,1,0,1,2],[1,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        True
        >>> a_gagne_diag2([[1,1,2,2,2,1,1],[2,1,2,2,1,2,2],[2,2,1,1,0,1,2],[2,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        True
        >>> a_gagne_diag2([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        False
    """
    # Retourne automatiquement False si les dimensions de la grille sont inférieures à 4x4 pcq il n'y a pas de diagonales dans une grille de telles dimensions
    if len(grille[0]) < 4 or len(grille) < 4:
        return False
    
    # Chaque fois qu'on voit un pion du joueur on teste sa diagonale montante
    for line in range(3,len(grille)):               # On réduit la grille de recherche aux départs possibles de diagonales
        for column in range(len(grille[0])-3):      # Idem
            if grille[line][column] == joueur:
                if grille[line-1][column+1] == grille[line-2][column+2] == grille[line-3][column+3] == joueur:
                    return True
    return False

def a_gagne(grille,joueur) :
    """
        Étant donné une grille et un joueur, retourne True si le joueur a gagné peut importe comment

        :param grille: grille à tester
        :param joueur: joueur dont la victoire est à tester
        :type grille: list
        :type joueur: int
        :return: ce joueur a-t-il gagné ?
        :rtype: bool

        .. seealso:: a_gagne_vert(grille,joueur), a_gagne_hor(grille,joueur), a_gagne_hor(grille,joueur), a_gagne_diag2(grille,joueur)

        :Example:

        >>> a_gagne([[1,1,2,1,2,1,1],[2,1,2,2,1,2,1],[0,2,2,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        True
        >>> a_gagne([[1,1,2,2,2,1,1],[2,1,2,2,1,2,2],[2,2,1,1,0,1,2],[2,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],2)
        True
        >>> a_gagne([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]],1)
        False
    """
    return a_gagne_vert(grille,joueur) or a_gagne_hor(grille,joueur) or a_gagne_diag1(grille,joueur) or a_gagne_diag2(grille,joueur)

def grille_pleine(grille) :
    """
        Étant donné une grille, retourne True si la grille est pleine (draw), False sinon

        :param grille: grille à tester
        :type grille: list
        :return: draw ?
        :rtype: bool

        :Example:

        >>> grille_pleine([[1,1,2,1,2,1,1],[2,1,2,2,1,2,2],[0,2,1,1,0,1,2],[0,1,2,2,0,0,0],[0,1,2,1,0,0,0],[0,0,0,0,0,0,0]])
        False
        >>> grille_pleine([[1,1,1,2],[1,1,1,2],[2,2,2,1],[2,2,2,1]])
        True
    """
    for el in grille:
        if 0 in el:
            return False
    return True

def boucle_principale() :
    # Générer la grille
    grille = generer_grille_vide(5,5)

    # Set le joueur qui commence
    joueur_courant = 1

    # On joue jusqu'à ce que le grille soit pleine
    while not grille_pleine(grille):
        # Affichage de la grille
        affiche_grille(grille)

        # Input du joueur
        coup_courant = int(input(f"Au tour du joueur {joueur_courant}:\nJouer dans la colonne : "))

        # Affiche une erreur jusqu'à ce que le joueur entre une input valide
        while not peut_jouer(grille,coup_courant):
            print("----------COUP INVALIDE----------\n  Colonne invalide\nou\n  Colonne peut-être pleine\n---------------------------------")
            affiche_grille(grille)
            coup_courant = int(input(f"Toujours au tour du joueur {joueur_courant}:\nJouer dans la colonne : "))

        # Joue le coup
        joue(grille,coup_courant,joueur_courant)    # todo : grille = or not ?

        # Vérifie si le joueur courant a gagné
        if a_gagne(grille,joueur_courant):
            print(f"----------VICTOIRE----------\nLe joueur {joueur_courant} a gagné !\n----------------------------")
            return True
        
        # Change de joueur courant
        if joueur_courant == 1:
            joueur_courant = 2
        else:
            joueur_courant = 1
    
    # La grille est pleine (out de la loop) donc draw
    print("----------MATCH NUL----------\nÉgalité parfaite entre le joueur 1 et le joueur 2")

if __name__ == "__main__" :
    doctest.testmod()
    boucle_principale()