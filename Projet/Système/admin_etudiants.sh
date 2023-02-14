# Projet 2 : Génération de comptes étudiants

# Vérification et récupération des arguments -----------------------------------
# Vérification du nombre d'arguments
if [ $# -ne 2 ]; then
    echo "Nombre d'arguments incorrect : $# donné(s), 2 attendus"
    echo "Syntaxe attendue : bash admin_etudiants.sh <liste> <dossier>"
    exit 1
fi

# Vérification de l'existence des fichiers
if [ ! -f $1 ]; then
    echo "Le fichier entré en paramètre n'existe pas"
    echo "Syntaxe attendue : bash admin_etudiants.sh <liste> <dossier>"
    exit 1
fi

if [ ! -d $2 ]; then
    echo "Le dossier entré en paramètre n'existe pas"
    echo "Syntaxe attendue : bash admin_etudiants.sh <liste> <dossier>"
    exit 1
fi

# Récupération des arguments du script
FILE=$1
DIR=$2

# Fonctions --------------------------------------------------------------------
# Génération mot de passe
function password(){
    MDP=""

    # On génère une liste random de consonnes, de voyelles et de chiffres
    RANDOM_CONS=$(head -n 10 /dev/urandom | tr -d -c 'bcdfghjklmnpqrstvwxz')
    RANDOM_VOY=$(head -n 10 /dev/urandom | tr -d -c 'aeiouy')
    RANDOM_NBR=$(head -n 10 /dev/urandom | tr -d -c '0123456789')

    # On prend les 2 premiers caractères de chaque liste de cons et de voy random et on les alterne pour avoir le bon pattern (c v c v)
    for i in {1..2}; do
        MDP=$MDP${RANDOM_CONS:$[$i - 1]:1}${RANDOM_VOY:$[$i - 1]:1}
    done
    
    # On génère les 4 chiffres à partir de la liste de nbrs randoms
    for i in {1..4}; do
        MDP=$MDP${RANDOM_NBR:$[$i -1]:1}
    done

    echo $MDP
}

# Génèration du dossier personnel (param1:pseudo)
function create_dir(){
    mkdir $1                # Création du dossier principal
    mkdir $1/Documents      # Création du dossier documents
    mkdir $1/Images         # Création du dossier images
    
    echo "mot de passe : $(password)" > $1/mot_de_passe.txt     # Création du .txt contenant le mdp
}

# Récupère le pseudo de l'étudiant (param1:ligne de la liste)
function get_pseudo(){
    # On récupère les noms et prénoms dans une ligne de la liste
    NOM=$(echo $1 | cut -d ";" -f 1)
    PRENOM=$(echo $1 | cut -d ";" -f 2)

    # On supprime les caractères spéciaux et les espaces
    NOM=$(echo $NOM | tr -d "[:punct:]" | tr -d " ")      
    PRENOM=$(echo $PRENOM | tr -d "[:punct:]" | tr -d " ")
    
    PART1=${PRENOM:0:2}     # 2 premiers caractères du prénom
    PART2=${NOM:0:7}        # 7 premiers caractère du nom
    PSEUDO=$PART1$PART2     # Concaténation des deux
    echo $PSEUDO
}

# Main -------------------------------------------------------------------------
function main(){
    cat $FILE | while read LINE; do
        create_dir "$DIR/$(get_pseudo "$LINE")"    # Création du dossier perso grâce à la fonction create_dir qui prend en paramètre le pseudo de get_pseudo
    done
    echo "Opération terminée"
}

# Execution --------------------------------------------------------------------
main