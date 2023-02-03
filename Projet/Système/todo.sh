# Projet 1 : TODO Liste
#!/bin/bash

SAVE_FILE=$HOME/.todo_list.txt

# Main
function todo(){
    #------------------------------------------------------------
    # list : Afficher la liste des tâches
    if [ $1 == "list" ]; then
        # Vérification de l'exitence du fichier
        if [ ! -f $SAVE_FILE ]; then
            touch $SAVE_FILE
        fi

        # Vérification du nombre d'arguments
        if [ $# -ne 1 ]; then
            echo "Nombre d'argument(s) incorrect :"
            echo "$[$# - 1] argument(s) donné(s), 0 attendu"
            echo "Utilisez la commande \"help\" pour obtenir de l'aide"
            return 1
        fi

        # Affichage
        if [ ! -s $SAVE_FILE ]; then
            echo "La liste est vide"
            echo "Utilisez la commande \"add\" pour ajouter une tâche"
        else
            echo "Liste de tâches en attente :"
            nl -w 1 -s " - " $SAVE_FILE
        fi

    #------------------------------------------------------------
    # done : Supprimer une tâche
    elif [ $1 == "done" ]; then
        LENGTH_SAVE_FILE=$(wc -l < $SAVE_FILE)

        # Vérification de l'existence du fichier
        if [ ! -f $SAVE_FILE ]; then
            echo "La liste est déjà vide, il n'y a pas de tâches à supprimer"
            echo "Utilisez la commande \"add\" pour ajouter une tâche"
            return 1
        fi

        # Si la liste est vide
        if [ ! -s $SAVE_FILE ]; then
            echo "La liste est déjà vide, il n'y a pas de tâches à supprimer"
            echo "Utilisez la commande \"add\" pour ajouter une tâche"
            return 1
        fi

        # Vérification du nombre d'argument
        if [ $# -ne 2 ]; then
            echo "Nombre d'argument(s) incorrect : "
            echo "$[$# - 1] argument(s) donné(s), 1 attendu"
            echo "Utilisez la commande \"help\" pour obtenir de l'aide"
            return 1
        fi

        # Vérification du type de l'argument
        if ! [[ $2 =~ ^[0-9]+$ ]]; then
            echo "Argument invalide : "
            echo "La position doit être un nombre entier"
            echo "Utilisez la commande \"help\" pour obtenir de l'aide"
            return 1
        fi

        # Vérification de l'existence de la tâche entrée
        if [ $2 -gt $LENGTH_SAVE_FILE ] || [ $2 -lt 1 ]; then
            echo "Position invalide, il y a actuellement $LENGTH_SAVE_FILE tâche(s) en attente"
            echo "Utilisez la commande \"list\" pour afficher la liste des tâches"
            return 1
        fi

        # Supression de la tâche
        TASK_TO_DEL=$(head -n $2 $SAVE_FILE | tail -1)

        head -n $[$2 - 1] $SAVE_FILE > ~/.temp_todo.txt
        tail -n $[$LENGTH_SAVE_FILE - $2] $SAVE_FILE >> ~/.temp_todo.txt
        mv ~/.temp_todo.txt $SAVE_FILE  

        #Affichage
        echo "La tâche $2 ($TASK_TO_DEL) a été supprimée"

    #------------------------------------------------------------
    # add : Ajouter une tâche
    elif [ $1 == "add" ]; then
        POS=$2
        LENGTH_SAVE_FILE=$(wc -l < $SAVE_FILE)
        MESSAGE=""

        # Vérification de l'existence du fichier
        if [ ! -f $SAVE_FILE ]; then
            touch $SAVE_FILE
        fi

        # Vérification du nombre d'argument
        if [ $# -lt 3 ]; then
            echo "Nombre d'argument(s) incorrect : "
            echo "$[$# - 1] argument(s) donné(s), au moins 2 attendu"
            echo "Utilisez la commande \"help\" pour obtenir de l'aide"
            return 1
        fi

        # Vérification du type des arguments
        if ! [[ $2 =~ ^[0-9]+$ ]]; then
            echo "Argument invalide : "
            echo "La position doit être un nombre entier"
            echo "Utilisez la commande \"help\" pour obtenir de l'aide"
            return 1
        fi

        # Vérification de la position d'entrée
        if [ $2 -lt 1 ]; then
            echo "Position invalide (négative ou nulle), il y a actuellement $LENGTH_SAVE_FILE tâche(s) en attente"
            echo "Utilisez la commande \"list\" pour afficher la liste des tâches"
            return 1

        # Si la position est supérieure au nombre de tâches
        elif [ $2 -gt $[$LENGTH_SAVE_FILE +1] ]; then
            POS=$[$LENGTH_SAVE_FILE +1]
            MESSAGE="(fin de liste)"
        fi

        # Ajout de la tâche
        TASK_TO_ADD=${@:3}

        head -n $[$POS - 1] $SAVE_FILE > ~/.temp_todo.txt
        echo $TASK_TO_ADD >> ~/.temp_todo.txt
        tail -n $[$LENGTH_SAVE_FILE - $POS + 1] $SAVE_FILE >> ~/.temp_todo.txt

        mv ~/.temp_todo.txt $SAVE_FILE

        # Affichage
        echo "La tâche ($TASK_TO_ADD) a été ajoutée en position $POS $MESSAGE"

    #------------------------------------------------------------
    # help : Afficher la liste des commandes
    elif [ $1 == "help" ]; then
        echo "Liste des commandes :"
        echo "  Afficher la liste des tâches    : todo list"
        echo "  Supprimer une tâche             : todo done <position>"
        echo "  Ajouter une tâche               : todo add <position> <tâche>"
        echo "  Afficher la liste des commandes : todo help"

    #------------------------------------------------------------
    # Si la commande n'est pas reconnue
    else
        echo "Commande inconnue : $1"
        echo "Utilisez la commande \"help\" pour obtenir de l'aide"
    fi
}