# Projet 1 : TODO Liste
#!/bin/bash

SAVE_FILE=$HOME/.todo_list_default.txt

# Main
function todo(){
    # Si aucun argument n'est donné : affiche une aide
    if [ $# -eq 0 ]; then
        echo "Bienvenue votre TODO liste !"
        echo "Vous pouvez :"
        echo "Afficher la liste des tâches : \"todo list\""
        echo "Ajouter une tâche : \"todo add <position> <tâche>\""
        echo "Supprimer une tâche : \"todo done <position>\""
        echo "Gérer les listes : \"todo manager\""
        echo "Afficher l'aide : \"todo help\""
        return 0

    else
        #------------------------------------------------------------
        # manager : Gérer les fichiers de sauvegarde
        if [ $1 = "manager" ]; then
            # S'il n'y qu'un argument : affiche une aide
            if [ $# -eq 1 ];then
                echo "Gestionnaire de listes"
                echo "  Afficher la liste des listes :  todo manager view"
                echo "  Créer une nouvelle liste :      todo manager create <nom_de_la_liste>"
                echo "  Supprimer une liste existante : todo manager delete <nom_de_la_liste>"
                echo "  Changer de liste :              todo manager switch <nom_de_la_liste>"
                echo "  Utiliser la liste par défaut :  todo manager default"
                return 0
            fi

            # default
            if [ $2 = "default" ]; then
                # Vérification du nombre d'arguments
                if [ $# -ne 2 ]; then
                    echo "Nombre d'argument(s) incorrect :"
                    echo "$[$# - 1] argument(s) donné(s) pour default, 0 attendu"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                if [ ! -f $HOME/.todo_list_default.txt ]; then
                    touch $HOME/.todo_list_default.txt
                fi

                SAVE_FILE=$HOME/.todo_list_default.txt
                echo "Vous êtes maintenant sur la liste par défaut"

            # view
            elif [ $2 = "view" ]; then
                # Vérification du nombre d'arguments
                if [ $# -ne 2 ]; then
                    echo "Nombre d'argument(s) incorrect :"
                    echo "$[$# - 1] argument(s) donné(s) pour view, 0 attendu"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Si aucune liste n'a été créée
                if ! ls $HOME/.todo_list_*.txt 1> /dev/null 2>&1; then
                    echo "Aucune liste existante"
                    echo "Utilisez la commande \"manager create\" pour créer une liste"
                    return 0
                
                # Affichage des listes avec la liste courante mise en valeur
                else
                    echo "Listes disponibles :"
                    for file in $HOME/.todo_list_*.txt; do
                        if [ $file = $SAVE_FILE ]; then
                            echo -e "- $(basename $file | sed 's/.txt//' | sed 's/.todo_list_//')\e[31m <--liste courante\e[0m"
                        else
                            echo "- $(basename $file | sed 's/.txt//' | sed 's/.todo_list_//')"
                        fi
                    done
                    return 0
                fi

            # create
            elif [ $2 = "create" ]; then
                # Vérification du nombre d'arguments
                if [ $# -ne 3 ]; then
                    echo "Nombre d'argument(s) incorrect :"
                    echo "$[$# - 1] argument(s) donné(s) pour create, 1 attendu"
                    echo "Caractères autorisés : a-z, A-Z, 0-9, _"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Si le nom de la liste contient des caractères non autorisés
                if [[ $3 =~ [^a-zA-Z0-9_] ]]; then
                    echo "Nom de liste invalide :"
                    echo "Caractères autorisés : a-z, A-Z, 0-9, _"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Si la liste existe déjà
                if [ -f $HOME/.todo_list_$3.txt ]; then
                    echo "Liste \"$3\" existante"
                    echo "Utilisez la commande \"mananger view\" pour obtenir la liste des listes"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Basculement sur cette nouvelle liste
                SAVE_FILE=$HOME/.todo_list_$3.txt

                # Création de la liste
                touch $HOME/.todo_list_$3.txt
                echo "Liste \"$3\" créée, vous êtes maintenant sur cette liste"
                return 0
            
            # delete
            elif [ $2 = "delete" ]; then
                # Vérification du nombre d'arguments
                if [ $# -ne 3 ]; then
                    echo "Nombre d'argument(s) incorrect :"
                    echo "$[$# - 1] argument(s) donné(s) pour delete, 1 attendu"
                    echo "Utilisez la commande \"mananger view\" pour obtenir la liste des listes"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Si la liste n'existe pas
                if [ ! -f $HOME/.todo_list_$3.txt ]; then
                    echo "Liste \"$3\" inexistante"
                    echo "Utilisez la commande \"mananger view\" pour obtenir la liste des listes"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Suppression de la liste
                rm $HOME/.todo_list_$3.txt
                echo "Liste \"$3\" supprimée"
                return 0

            # switch
            elif [ $2 = "switch" ]; then
                # Vérification du nombre d'arguments
                if [ $# -ne 3 ]; then
                    echo "Nombre d'argument(s) incorrect :"
                    echo "$[$# - 1] argument(s) donné(s) pour switch, 1 attendu"
                    echo "Utilisez la commande \"mananger view\" pour obtenir la liste des listes"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Si la liste n'existe pas
                if [ ! -f $HOME/.todo_list_$3.txt ]; then
                    echo "Liste \"$3\" inexistante"
                    echo "Utilisez la commande \"mananger view\" pour obtenir la liste des listes"
                    echo "Utilisez la commande \"manager\" pour obtenir de l'aide"
                    return 1
                fi

                # Changement de liste
                SAVE_FILE=$HOME/.todo_list_$3.txt
                echo "Liste \"$3\" sélectionnée"
                return 0
            
            # Si il y a trop d'arguments
            elif [ $# -gt 3 ]; then
                echo "Nombre d'argument(s) incorrect :"
                echo "$[$# - 1] argument(s) donné(s), 2 attendu"
                echo "Utilisez la commande \"todo manager\" pour obtenir de l'aide"
                return 1
            
            # Mauvais argument
            else
                echo "Argument invalide :"
                echo "Utilisez la commande \"todo manager\" pour obtenir de l'aide"
                return 1
            fi

        #------------------------------------------------------------
        # list : Afficher la liste des tâches
        elif [ $1 = "list" ]; then
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
            TASK_TO_DEL=$(head -n $2 $SAVE_FILE | tail -1)

            head -n $[$2 - 1] $SAVE_FILE > ~/.temp_todo.txt
            tail -n $[$LENGTH_SAVE_FILE - $2] $SAVE_FILE >> ~/.temp_todo.txt
            mv ~/.temp_todo.txt $SAVE_FILE  

            #Affichage
            echo "La tâche $2 ($TASK_TO_DEL) est faite !"
            return 0

        #------------------------------------------------------------
        # add : Ajouter une tâche
        elif [ $1 = "add" ]; then
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
            echo "  Gérer les listes de tâches      : todo manager"
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