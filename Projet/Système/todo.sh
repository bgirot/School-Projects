# Projet 1 : TODO Liste
#!/bin/bash

SAVE_FILE=$HOME/.todo_list

# Main
function todo(){
    # Si aucun argument n'est donné : affiche une aide
    if [ $# -eq 0 ]; then
        echo "Bienvenue votre TODO liste !"
        echo "Vous pouvez :"
        echo "Afficher la liste des tâches : \"todo list\""
        echo "Ajouter une tâche : \"todo add <position> <tâche>\""
        echo "Supprimer une tâche : \"todo done <position>\""
        echo "Afficher l'aide : \"todo help\""
        return 0

    else
        #------------------------------------------------------------
        # list : Afficher la liste des tâches
        if [ $1 = "list" ]; then
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
                return 0
            else
                echo "Liste de tâches en attente :"
                nl -w 1 -s " - " $SAVE_FILE
                return 0
            fi

        #------------------------------------------------------------
        # done : Supprimer une tâche
        elif [ $1 = "done" ]; then
            LENGTH_SAVE_FILE=$(wc -l < $SAVE_FILE)              # Longueur du fichier (nb de tâches)

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
                echo "La position doit être un nombre entier positif"
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
            TASK_TO_DEL=$(head -n $2 $SAVE_FILE | tail -1)                  # récupère la tâche à supprimer (av sa suppr pour pouvoir l'afficher)

            head -n $[$2 - 1] $SAVE_FILE > ~/.temp_todo                     # Ajoute les lignes avant la tâche à suppr dans un fichier temp
            tail -n $[$LENGTH_SAVE_FILE - $2] $SAVE_FILE >> ~/.temp_todo    # Ajoute les lignes après la tâche à suppr à la suite dans le temp
            mv ~/.temp_todo $SAVE_FILE                                      # On déplace le fichier temp vers le fichier main (ce qui suppr le temp)

            #Affichage
            echo "La tâche $2 ($TASK_TO_DEL) est faite !"
            return 0

        #------------------------------------------------------------
        # add : Ajouter une tâche
        elif [ $1 = "add" ]; then
            POS=$2                                      # Conserve la position car elle risque d'être modifiée dans le cas où pos > nb_ligne
            LENGTH_SAVE_FILE=$(wc -l < $SAVE_FILE)      # Longueur du fichier (correspond au nombre de tâches)
            MESSAGE=""                                  # Contiendra le message de la position

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
                echo "La position doit être un nombre entier positif"
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
                POS=$[$LENGTH_SAVE_FILE+1]                                      # Def la pos comme la pos de la fin du fichier
                MESSAGE="(fin de liste)"                                        # Custom le message de fin
            fi

            # Ajout de la tâche
            TASK_TO_ADD=${@:3}                                                  # Récupère la tâche à ajouter pour l'afficher plus tard

            head -n $[$POS - 1] $SAVE_FILE > ~/.temp_todo                       # Ajoute les tâches avant la pos de celle à ajouter dans un temp
            echo $TASK_TO_ADD >> ~/.temp_todo                                   # Ajoute la tâche à ajouter en pos demandée à la suite du temp
            tail -n $[$LENGTH_SAVE_FILE - $POS + 1] $SAVE_FILE >> ~/.temp_todo  # Ajoute la fin du fichier à la suite

            mv ~/.temp_todo $SAVE_FILE                                          # Déplace

            # Affichage
            echo "La tâche ($TASK_TO_ADD) a été ajoutée en position $POS $MESSAGE"
            return 0

        #------------------------------------------------------------
        # help : Afficher la liste des commandes
        elif [ $1 = "help" ]; then
            # Vérification du nombre d'argument
            if [ $# -ne 1 ]; then
                echo "Nombre d'argument(s) incorrect : "
                echo "$[$# - 1] argument(s) donné(s), 0 attendu"
                echo "Utilisez la commande \"help\" pour obtenir de l'aide"
                return 1
            fi

            # Affichage
            echo "Liste des commandes :"
            echo "  Afficher la liste des tâches    : todo list"
            echo "  Supprimer une tâche             : todo done <position>"
            echo "  Ajouter une tâche               : todo add <position> <tâche>"
            echo "  Rechercher une tâche            : todo search <recherche>"
            echo "  Afficher la liste des commandes : todo help"
            
            return 0

        #------------------------------------------------------------
        # Filtre pour trouver une tâche précise avec un mot clé
        elif [ $1 = "search" ]; then
            # Vérification de l'existence du fichier
            if [ ! -f $SAVE_FILE ]; then
                echo "La liste est vide, il n'y a pas de tâche à rechercher"
                echo "Utilisez la commande \"add\" pour ajouter une tâche"
                return 1
            fi

            # Si la liste est vide
            if [ ! -s $SAVE_FILE ]; then
                echo "La liste est vide, il n'y a pas de tâche à rechercher"
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

            # Recherche avec pour affichage : <position> - <tâche>
            grep --color=always -n $2 $SAVE_FILE | sed 's/:/ - /'
            return 0

        #------------------------------------------------------------
        # Si la commande n'est pas reconnue
        else
            echo "Commande inconnue : $1"
            echo "Utilisez la commande \"help\" pour obtenir de l'aide"
            return 0
        fi
    fi
}