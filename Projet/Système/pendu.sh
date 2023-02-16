# Projet 3 : Jeu du pendu
#!/bin/bash

# Vérification et récupération des arguments -------------------------------------
# Vérification du nombre d'arguments
if [ $# -ne 1 ]; then
    echo "Nombre d'arguments incorrect : $# donné(s), 1 attendu"
    echo "Syntaxe attendue : bash pendu.sh <dictionnaire>"
    exit 1
fi

# Vérification de l'existence du fichier
if [ ! -f $1 ]; then
    echo "Le fichier entré en paramètre n'existe pas"
    echo "Syntaxe attendue : bash pendu.sh <dictionnaire>"
    exit 1
fi

DICT=$1     # Récupération du dictionnaire

# Création des 10 stades de pénalité --------------------------------------------
declare -a PENALITY=(
    "\n\n\n\n\n\n"
    "\n\n\n\n\n___ ___"
    "\n   |\n   |\n   |\n   |\n___|___"
    "    _____\n   |\n   |\n   |\n   |\n___|___"
    "    _____\n   |     |\n   |\n   |\n   |\n___|___"
    "    _____\n   |     |\n   |     O\n   |\n   |\n___|___"
    "    _____\n   |     |\n   |     O\n   |     |\n   |\n___|___"
    "    _____\n   |     |\n   |     O\n   |    /|\n   |\n___|___"
    "    _____\n   |     |\n   |     O\n   |    /|\\ \n   |\n___|___"
    "    _____\n   |     |\n   |     O\n   |    /|\\ \n   |    / \n___|___"
    "    _____\n   |     |\n   |     O\n   |    /|\\ \n   |    / \\ \n___|___"
)

# Fonctions --------------------------------------------------------------------
function display(){
    echo -e "******************************\n"                          # Affichage du divider
    echo -e "${PENALITY[$FAILED_ATTEMPS]}\n"                            # Affichage du dessin de pénalité courant
    echo -e "Lettres testées : $TESTED_LETTERS\n"                       # Affichage des lettres testées
    echo $WORD_TO_FIND
    echo -e "$WORD_TO_FIND" | tr "$NOT_TESTED_LETTERS" "_"           # Affichage du mot à trouver
}

function testLetter(){
    # Gestion des erreurs (une seule lettre et une lettre pas un chiffre)
    if [ ${#LETTER} -ne 1 ] || ! [[ "$LETTER" =~ [A-Z] ]]; then
        echo "Erreur : vous devez entrer une seule lettre qui soit en majuscule"
        return
    fi

    # Si la lettre a déjà été testée
    if [[ "$TESTED_LETTERS" =~ "$LETTER" ]]; then
        echo "La lettre $LETTER a déjà été testée"
        FAILED_ATTEMPS=$[$FAILED_ATTEMPS+1]

    # Si la lettre n'est pas dans le mot
    elif ! [[ "$WORD_TO_FIND" =~ "$LETTER" ]]; then
        TESTED_LETTERS+="$LETTER "
        echo "La lettre $LETTER n'est pas de le mot recherché"
        FAILED_ATTEMPS=$[$FAILED_ATTEMPS+1]

    # Si la lettre est dans le mot
    elif [[ "$WORD_TO_FIND" =~ "$LETTER" ]]; then
        TESTED_LETTERS+="$LETTER "
        NOT_TESTED_LETTERS=$(echo $NOT_TESTED_LETTERS | sed "s/$LETTER//")
        # Si le joueur gagne sur ce coup
        if [ $(echo $WORD_TO_FIND | tr "$NOT_TESTED_LETTERS" "_" | grep -o "_" | wc -l) -eq 0 ]; then
            echo -e "\nVous avez gagné !"
            exit 0
        else
            echo "La lettre $LETTER est dans le mot recherché"
        fi
    fi
}

# Main -------------------------------------------------------------------------
function main(){
    WORD_TO_FIND=$(head -n $[$RANDOM%$(wc -l < $DICT)+1] $DICT | tail -n 1)     # Génération du mot aléatoire
    FAILED_ATTEMPS=0
    TESTED_LETTERS=""
    NOT_TESTED_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    display 

    while [ $FAILED_ATTEMPS -lt 10 ]; do
        read -p "Choisissez une lettre : " LETTER
        testLetter
        display
    done

    echo -e "\nVous avez perdu !"
}

main        # Exécution