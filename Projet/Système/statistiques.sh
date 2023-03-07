# Projet 5 : Statistiques sur les fichiers
#!/bin/bash

# Fonction statisitiques -----------------------------------------------------
function statistiques(){
    DIR_TO_ANALYSE=$(pwd)

    # Vérification des arguments ---------------------------------------------
    # S'il n'y a pas précisément 1 argument
    if [ $# -gt 1 ]; then
        echo "Nombre d'arguments incorrect"
        echo "$# argument(s) donné(s), 1 attendu"
        echo "Syntaxe attendue : statistiques <détail du rapport>"
        echo "  - statistiques 1 : faible niveau de détail"
        echo "  - statistiques 2 : niveau de détail moyen"
        echo "  - statistiques 3 : niveau de détail élevé"
        return 1

    # statistiques 1 (faible niveau de détail) -------------------------------
    elif [ $# -eq 0 ] || [ $1 -eq 1 ]; then
        echo "Analyse de $DIR_TO_ANALYSE :"

        # Nombre de répertoires
        echo "  - $[$(find $DIR_TO_ANALYSE -type d | wc -l) - 1] répertoire(s)"

        # Nombre de fichiers
        echo "  - $(find $DIR_TO_ANALYSE -type f | wc -l) fichier(s)"

        # Taille totale
        echo "  - Taille totale : $(du -sh $DIR_TO_ANALYSE | cut -f1)"

    # statistiques 2 (niveau de détail moyen) -------------------------------
    elif [ $1 == "2" ]; then
        echo "Analyse de $DIR_TO_ANALYSE :"

        # Nombre de répertoires dont répertoires cachés et vides
        echo "  - $[$(find $DIR_TO_ANALYSE -type d | wc -l) - 1] répertoire(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type d -name ".*" | wc -l)] répertoire(s) caché(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type d -empty | wc -l)] répertoire(s) vide(s)"

        # Nombre de fichier dont fichiers cachés et vides
        echo "  - $(find $DIR_TO_ANALYSE -type f | wc -l) fichier(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type f -name ".*" | wc -l)] fichier(s) caché(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type f -empty | wc -l)] fichier(s) vide(s)"

        # Taille totale
        echo "  - Taille totale : $(du -sh $DIR_TO_ANALYSE | cut -f1)"

    # statistiques 3 (niveau de détail élevé) -------------------------------
    elif [ $1 == "3" ]; then
        echo "Analyse de $DIR_TO_ANALYSE :"

        # Nombre de répertoires dont répertoires cachés et vides
        echo "  - $[$(find $DIR_TO_ANALYSE -type d | wc -l) - 1] répertoire(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type d -name ".*" | wc -l)] répertoire(s) caché(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type d -empty | wc -l)] répertoire(s) vide(s)"

        # Nombre de fichier dont fichiers cachés et vides
        echo "  - $(find $DIR_TO_ANALYSE -type f | wc -l) fichier(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type f -name ".*" | wc -l)] fichier(s) caché(s)"
        echo "      - $[$(find $DIR_TO_ANALYSE -type f -empty | wc -l)] fichier(s) vide(s)"
        # fichiers de moins de 512 ko
        echo "      - $[$(find $DIR_TO_ANALYSE -type f -size -512k | wc -l)] fichier(s) de moins de 512 ko"
        # fichiers de plus de 15 Mo
        echo "      - $[$(find $DIR_TO_ANALYSE -type f -size +15M | wc -l)] fichier(s) de plus de 15 Mo"
        #  le plus gros fichier
        echo -e "      - Le plus gros fichier est :\n         $(find $DIR_TO_ANALYSE -type f -exec ls -l {} + | sort -k 5 -rn | head -n 1 | awk '{print $NF}')"

        echo -e "\n      Il y a :"
        # Nombre de fichiers python
        echo "         - $(find $DIR_TO_ANALYSE -type f -name "*.py" | wc -l) fichier(s) python"
        # Nombre de fichiers video (mp4, avi, mkv)
        echo "         - $(find $DIR_TO_ANALYSE -type f -name "*.mp4" -o -name "*.avi" -o -name "*.mkv" | wc -l) fichier(s) vidéo"
        # Nombre de fichiers image (jpeg, jpg, png, gif)
        echo "         - $(find $DIR_TO_ANALYSE -type f -name "*.jpeg" -o -name "*.jpg" -o -name "*.png" -o -name "*.gif" | wc -l) fichier(s) image"
        # Taille totale
        echo "  - Taille totale : $(du -sh $DIR_TO_ANALYSE | cut -f1)"

    
    # Si l'argument n'est pas valide ----------------------------------------
    else
        echo "Argument invalide : $1"
        echo "Syntaxe attendue : statistiques <détail du rapport>"
        echo "  - statistiques 1 : faible niveau de détail"
        echo "  - statistiques 2 : niveau de détail moyen"
        echo "  - statistiques 3 : niveau de détail élevé"
        return 1
    fi
}