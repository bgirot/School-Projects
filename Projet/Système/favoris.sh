# Projet 4 : Gestion des dossiers favoris
#!/bin/bash

SAVE_FILE=$HOME/.favoris_bash

# Fonction L (list) -------------------------------------------------------------
function L(){
    # Si aucun argument n'est donné :
    if [ $# -eq 0 ]; then
        if [ ! -s $SAVE_FILE ]; then
            echo "Aucun favori enregistré"
        else
            echo -e "\e[4mListe des favoris enregistrés :\e[0m\n"
            nl -w 1 -s '- ' $SAVE_FILE | sed 's/^[0-9]\+\s*//' | sed 's/->.*$/-/' | sed 's/.$//'
        fi

    # Argument -p (afficher les chemins des favoris)
    elif [ $1 == "-p" ] && [ $# -eq 1 ]; then
        if [ ! -s $SAVE_FILE ]; then
            echo "Aucun favori enregistré"
        else
            echo -e "\e[4mListe des favoris enregistrés (avec leurs chemins) :\e[0m\n"
            nl -w 1 -s '- ' $SAVE_FILE
        fi
    
    # Argument -s (rechercher une string parmi les favoris)
    elif [ $1 == "-s" ] && [ $# -eq 2 ]; then
        if [ ! -s $SAVE_FILE ]; then
            echo "Aucun favori enregistré"

        else
            SEARCH_FIELD="$(cat $SAVE_FILE | cut -d ">" -f 1 | sed 's/.$//')"   # Champ de recherche (sans les paths qui pourraient fausser la recherche)
            SEARCH_RESULT="$(grep -i $2 <<< $SEARCH_FIELD)"                     # Résultat de la recherche

            if [ "$SEARCH_RESULT" == "" ]; then
                echo "Aucun favori ne contient \"$2\""
            else
                echo -e "\e[4mListe des favoris enregistrés contenant \"$2\" :\e[0m\n"
                grep -i $2 <<< $SEARCH_FIELD   # On ne réutilise pas SEARCH_RESULT pour conserver la syntaxe de grep qui est mieux
            fi
        fi

    # Si erreur dans les arguments
    else
        echo "Argument(s) invalide(s) :"
        echo "Syntaxe attendue : L [OPTION]"
        echo "Options disponibles :"
        echo "  -p      affiche la liste des raccourcis avec leurs chemins respectifs"
        echo "  -s      affiche la liste des raccourcis contenant la chaîne (sans espace) donnée"
    fi
}

# Fonction S (save) -------------------------------------------------------------
function S(){
    # S'il y a bien un seul argument
    if [ $# -eq 1 ]; then
        # Todo : vérifier que le raccourci existe pas déjà
        if [ "$(grep -w $1 $SAVE_FILE)" != "" ]; then
            echo "Le raccourci \"$1\" existe déjà"
            echo "Utilisez la commande R pour le supprimer"
            return 1
        fi

        echo "$1->$(pwd)" >> $SAVE_FILE  # Ajout du raccourci dans le fichier
        echo -e "Le répertoire $(pwd) est sauvegardé dans vos favoris.\n  -> raccourci : $1"

    # Si erreur dans les arguments
    else
        echo "Nombre d'argumement(s) invalide :"
        echo "1 argument attendu, $# donné(s)"
        echo "Syntaxe attendue : S <nom du raccourci>"
    fi
}

# Fonction R (remove) -----------------------------------------------------------
function R(){
    # S'il y a bien un seul argument
    if [ $# -eq 1 ]; then
        LINE_TO_REMOVE_NUMBER=$(grep -w -n $1 $SAVE_FILE | cut -d ":" -f 1) # Ligne à supprimer (on grep uniquement dans la liste des noms de raccourcis d'où le cut)
        SAVE_FILE_LENGTH=$(wc -l < $SAVE_FILE)                              # Nombre de lignes du fichier
        
        # Si le raccourci demandé n'existe pas
        if [ "$LINE_TO_REMOVE_NUMBER" == "" ]; then
            echo "Le favori \"$1\" n'existe pas"
            echo "Utilisez la commande L pour afficher la liste des favoris enregistrés"

        else
            head -n $[$LINE_TO_REMOVE_NUMBER - 1] $SAVE_FILE > ~/.temp_favoris                      # On redirige les lignes avant celle à suppr dans un temp
            tail -n $[$SAVE_FILE_LENGTH - $LINE_TO_REMOVE_NUMBER] $SAVE_FILE >> ~/.temp_favoris     # On redirgie les lignes après celle à suppr à la suite du temp
            mv ~/.temp_favoris $SAVE_FILE
            echo "Le favori \"$1\" a été supprimé de votre liste."
        fi
        
    # Si erreur dans les arguments
    else
        echo "Nombre d'argumement(s) invalide :"
        echo "1 argument attendu, $# donné(s)"
        echo "Syntaxe attendue : R <nom du raccourci>"
    fi
}

# Fonction C (change) -----------------------------------------------------------
# Désolé c'est immonde
function C(){
    # S'il y a bien un seul argument
    if [ $# -eq 1 ]; then
        SEARCH_FIELD="$(cat $SAVE_FILE | cut -d ">" -f 1 | sed 's/.$//')"   # Champ de recherche (sans les paths qui pourraient fausser la recherche)
        SEARCH_RESULT=$(grep -i $1 <<< $SEARCH_FIELD)                       # Résultat de la recherche

        # Si le raccourci demandé n'existe pas
        if [ "$SEARCH_RESULT" == "" ]; then
            echo "Le favori \"$1\" n'existe pas"
            echo "Utilisez la commande L pour afficher la liste des favoris enregistrés"

        # Si le raccourci demandé existe
        else
            # S'il n y a qu'un seul raccourci correspondant
            if [ $(echo "$(grep -i $1 <<< "$SEARCH_FIELD")" | wc -l) -eq 1 ]; then      # On cherche si le nombre de lignes du résultat de la recherche est égal à 1 (donc s'il n'y a qu'un seul raccourci correspondant)
                LINE_NUMBER=$(grep -n -i $1 <<< "$SEARCH_FIELD" | cut -d ":" -f 1)      # On récupère le numéro de la ligne correspondant au raccourci (qui est le meme que dans SAVE_FILE)
                cd "$(head -n $LINE_NUMBER $SAVE_FILE | tail -n 1 | cut -d ">" -f 2)"   # On change de répertoire (en prenant le path correspondant au raccourci depuis SAVE_FILE)

                echo -e "Vous êtes maintenant dans le répertoire\n$(pwd)"

            # S'il y a plus d'un raccourci correspondant...
            else
                # ...mais que la recherche était exacte
                if [ ! $(grep -w -i $1 <<< "$SEARCH_FIELD") == "" ]; then                   # On cherche si le nombre de lignes du résultat de la recherche est égal à 1 (donc s'il n'y a qu'un seul raccourci correspondant)
                    LINE_NUMBER=$(grep -w -n -i $1 <<< "$SEARCH_FIELD" | cut -d ":" -f 1)   # On récupère le numéro de la ligne correspondant au raccourci (qui est le meme que dans SAVE_FILE)
                    cd "$(head -n $LINE_NUMBER $SAVE_FILE | tail -n 1 | cut -d ">" -f 2)"   # On change de répertoire (en prenant le path correspondant au raccourci depuis SAVE_FILE)

                    echo -e "Vous êtes maintenant dans le répertoire\n$(pwd)"

                # ... et que la recherche n'était pas exacte, il y a donc plusieurs raccourcis correspondants
                else
                    echo "Plusieurs favoris correspondent à \"$1\""
                    echo "Utilisez la commande L -s <nom du raccourci> pour afficher la liste des favoris correspondants"
                fi
            fi
        fi

    # Si erreur dans les arguments
    else
        echo "Nombre d'argumement(s) invalide :"
        echo "1 argument attendu, $# donné(s)"
        echo "Syntaxe attendue : C <nom du raccourci>"
    fi
}