import matplotlib.pyplot as plt
import matplotlib.image as img

def neg(im) :
    """
        Fonction qui renvoie l'image négative de l'image im

        :param im: matrice correspondant à l'image de base
        :type im: list
        :return: matrice correspondant à l'image négative
        :rtype: list
    """
    return [1-y for y in [x for x in im]]       # On applique 1-x à la valeur chaque pixel

def miroir(im) :
    """
        Fonction qui renvoie l'image miroir de l'image im

        :param im: matrice correspondant à l'image de base
        :type im: list
        :return: matrice correspondant à l'image miroir
        :rtype: list
    """
    return [x[::-1] for x in im]                # On inverse l'ordre des pixels de chaque ligne

def plus_de_lumiere(im,d) :
    """
        Fonction qui renvoie l'image avec une augmentation de la luminosité de l'image im

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param d: valeur de l'augmentation de la luminosité
        :type d: float
        :return: matrice correspondant à l'image avec une augmentation de la luminosité
        :rtype: list
    """
    return [[max(0, min(1, y+d)) for y in x] for x in im]   # Ajoute d (une certaine lum) mais garde les valeurs entre 0 et 1

def plus_de_contraste(im,k) :
    """
        Fonction qui renvoie l'image avec un contraste augmenté de l'image im

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param k: valeur du contraste
        :type k: float
        :return: matrice correspondant à l'image avec un contraste augmenté
        :rtype: list
    """
    return [[max(0, min(1, y+k*(y-0.5))) for y in x] for x in im]   # Applique la fonction x + k*(x-0.5) 

def photomaton(im) :
    """
        Fonction qui renvoie le "photomatons" de l'image im (4 x l'image de base)

        :param im: matrice correspondant à l'image de base
        :type im: list
        :return: matrice correspondant à l'image avec une réduction de la taille
        :rtype: list
    """
    photomaton_matrix = [[y for y in x] for x in im]   # On copie la liste de base dans une autre variable
    n = len(im)//2                                     # On stocke la valeur de la moitié de la taille de la liste

    # On parcourt la liste et on remplace les valeurs par la valeur adaptée
    for i in range(2*n):                        
        for j in range(2*n):
            if i < n and j < n:
                photomaton_matrix[i][j] = im[2*i][2*j]
            elif i < n and j >= n:
                photomaton_matrix[i][j] = im[2*i][2*(j-n)+1]
            elif i >= n and j < n:
                photomaton_matrix[i][j] = im[2*(i-n)+1][2*j]
            else:
                photomaton_matrix[i][j] = im[2*(i-n)+1][2*(j-n)+1]

    return photomaton_matrix

def mlgk(im, k) :
    """
        Fonction qui renvoie le photomaton de l'image k fois

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param k: nombre de fois où on applique la fonction photomaton
        :type k: int
        :return: matrice correspondant à l'image avec une réduction de la taille
        :rtype: list

        :seealso: photomaton
    """
    return photomaton(im) if k == 1 else photomaton(mlgk(im, k-1))

# Réduction du nombre de couleurs
def f(x, b) :
    deux_b = 2**b
    return int(deux_b * int(255*x)/256)/(deux_b-1)

def moins_de_coul(im, b) :
    """
        Fonction qui renvoie l'image avec moins de couleurs

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param b: valeur de la réduction du nombre de couleurs
        :type b: int
        :return: matrice correspondant à l'image avec moins de couleurs
        :rtype: list

        :seealso: f
    """
    return [[f(y, b) for y in x] for x in im]

def moins_de_pix(im, k) :
    """
        Fonction qui renvoie l'image avec moins de pixels

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param k: valeur de la réduction du nombre de pixels
        :type k: int
        :return: matrice correspondant à l'image avec moins de pixels
        :rtype: list
    """
    # On parcourt l'image et on ne garde que les pixels dont l'indice est un multiple de k
    return [[im[i][j] for j in range(0, len(im), k)] for i in range(0, len(im), k)]

def moins_de_pix2(im, k) :
    """
        Fonction qui renvoie l'image avec moins de pixels en faisant la moyenne des pixels

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param k: valeur de la réduction du nombre de pixels
        :type k: int
        :return: matrice correspondant à l'image avec moins de pixels
        :rtype: list
    """
    matrix = [[0 for y in range(len(im)//k)] for x in range(len(im)//k)]

    for i in range(0, len(im)-k+1, k):
        for j in range(0, len(im)-k+1, k):
            # On calcule la moyenne des pixels dans le bloc que l'on réduit
            average_block = 0
            for x in range(k):
                for y in range(k):
                    average_block += im[i+x][j+y]
            matrix[i//k][j//k] = average_block
            
    return matrix

def mediane(sample):
    """
        Fonction qui renvoie la médiane d'une liste

        :param sample: liste de valeurs
        :type sample: list
        :return: valeur médiane
        :rtype: float
    """
    sample.sort()
    # Si la liste est paire, on renvoie la moyenne des deux valeurs centrales
    if len(sample)%2 == 0:
        return (sample[len(sample)//2 - 1] + sample[len(sample)//2])/2
    # Sinon on renvoie la valeur centrale
    else:
        return sample[len(sample)//2]

def get_neighbours(im, i, j, q):
    """
        Fonction qui renvoie les voisins d'un pixel
        Ici on considère le pixel central comme ne faisant pas partie du voisinnage

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param i: indice de la ligne du pixel en haut à gauche
        :type i: int
        :param j: indice de la colonne du pixel en haut à gauche
        :type j: int
        :param q: taille du voisinage
        :type q: int
        :return: liste des voisins du pixel
        :rtype: list
    """
    neighbours = []
    for x in range(-q, q+1):
        for y in range(-q, q+1):
            # On vérifie que le pixel est bien dans l'image et qu'il n'est pas le pixel central
            if i+x >= 0 and i+x < len(im) and j+y >= 0 and j+y < len(im) and (x != 0 or y != 0):
                neighbours.append(im[i+x][j+y])
    return neighbours

def filtre_median(im, q) :
    """
        Fonction qui renvoie l'image "lissée" par un filtre médian

        :param im: matrice correspondant à l'image de base
        :type im: list
        :param q: taille du voisinage
        :type q: int
        :return: matrice correspondant à l'image avec un filtre médian
        :rtype: list

        :seealso: mediane, get_neighbours
    """
    # On récupère les voisins avec get_neighbours et on calcule la médiane de ces voisins avec mediane
    return [[mediane(get_neighbours(im, i, j, q)) for j in range(len(im))] for i in range(len(im))]

def init(k) :
    """
        Fonction qui renvoie une matrice vide de taille 2^k

        :param k: taille de la matrice
        :type k: int
        :return: matrice vide
        :rtype: list
    """
    return [[0 for y in range(2**k)] for x in range(2**k)]

def arbre_to_image(qt,i,j,k,im) :
    """
        Fonction récurssive qui renvoie l'image corresondant au quadtree en paramètre

        :param qt: quadtree
        :type qt: list
        :param i: indice de la ligne du pixel en haut à gauche
        :type i: int
        :param j: indice de la colonne du pixel en haut à gauche
        :type j: int
        :param k: taille de la zone à convertir
        :type k: int
        :param im: matrice à remplir
        :type im: list
        :return: matrice remplie récursivement
        :rtype: list

        :seealso: init
    """
    # Si qt est un entier, on remplit la zone avec cette valeur
    if type(qt) == int:
        for x in range(i, i+(2**k)):
            for y in range(j, j+(2**k)):
                im[x][y] = qt

    # Si qt est une liste, on "plonge" dans les sous-arbres correspondants à chaque coins et on appelle la fonction récursivement
    else:
        arbre_to_image(qt[0], i, j, k-1, im)                        # Haut gauche
        arbre_to_image(qt[1], i, j+(2**(k-1)), k-1, im)             # Haut droit
        arbre_to_image(qt[2], i+(2**(k-1)), j, k-1, im)             # Bas gauche
        arbre_to_image(qt[3], i+(2**(k-1)), j+(2**(k-1)), k-1, im)  # Bas droit

def new_coul(x,nbc) :
    """
        Fonction qui renvoie l'entier correspondant au niveau de gris d'un pixel

        :param x: niveau de gris du pixel
        :type x: int
        :param nbc: nombre de niveaux de gris autorisés
        :type nbc: int
        :return: niveau de gris du pixel entier
        :rtype: int
    """
    return int(x*(nbc-1))

def test(im, i, j, k, nbc) :
    """
        Fonction qui vérifie si tous les pixels d'une zone sont de la même couleur

        :param im: matrice correspondant à l'image à analyser
        :type im: list
        :param i: indice de la ligne du pixel en haut à gauche
        :type i: int
        :param j: indice de la colonne du pixel en haut à gauche
        :type j: int
        :param k: taille de la zone à analyser
        :type k: int
        :param nbc: nombre de niveaux de gris autorisés
        :type nbc: int
        :return: booléen indiquant si tous les pixels sont de la même couleur et la couleur de la zone
        :rtype: tuple

        :seealso: new_coul
    """
    reference = new_coul(im[i][j], nbc)    # On prend le pixel en haut à gauche comme référence
    for x in range(i, i+(2**k)):
        for y in range(j, j+(2**k)):
            # Si un pixel n'est pas de la même couleur que la référence, on renvoie False (et -1 par précaution)
            if new_coul(im[x][y], nbc) != reference:
                return False, -1
    # Si tous les pixels sont de la même couleur, on renvoie True et la couleur de la zone
    return True, reference

def image_to_arbre(im, i, j, k, nbc) :
    """
        Fonction récursive qui renvoie le quadtree correspondant à une image

        :param im: matrice correspondant à l'image à convertir
        :type im: list
        :param i: indice de la ligne du pixel en haut à gauche
        :type i: int
        :param j: indice de la colonne du pixel en haut à gauche
        :type j: int
        :param k: taille de la zone à convertir
        :type k: int
        :param nbc: nombre de niveaux de gris autorisés
        :type nbc: int
        :return: quadtree correspondant à l'image
        :rtype: list

        :seealso: test
    """
    # Si tous les pixels sont de la même couleur, on renvoie cette couleur dans ke quadtree
    if test(im, i, j, k, nbc)[0]:
        return test(im, i, j, k, nbc)[1]
    
    # Sinon, on "explore" chqaue coin de la zone en appelant la fonction récursivement
    else:
        return [
            image_to_arbre(im, i, j, k-1, nbc),
            image_to_arbre(im, i, j+(2**(k-1)), k-1, nbc),
            image_to_arbre(im, i+(2**(k-1)), j, k-1, nbc),
            image_to_arbre(im, i+(2**(k-1)), j+(2**(k-1)), k-1, nbc)
            ]

def taille(qt) :
    """
        Fonction qui renvoie le nombre d'éléments d'un quadtree

        :param qt: quadtree
        :type qt: list
        :return: nombre d'éléments du quadtree
        :rtype: int
    """
    # Si qt est un entier, il n'y a qu'un élément
    if type(qt) == int:
        return 1
    # Sinon, on appelle la fonction récursivement sur chaque sous-arbre
    else:
        return taille(qt[0]) + taille(qt[1]) + taille(qt[2]) + taille(qt[3])

if __name__ == "__main__" :
    # Chargement de l'image june et conversion en niveau de gris
    june = img.imread('june.png')
    june = (june[:,:,0]+june[:,:,1]+june[:,:,2])/3

    # Chargement de l'image june_bruit et conversion en niveau de gris
    june_bruit = img.imread('juneBruit.png')
    june_bruit = (june_bruit[:,:,0]+june_bruit[:,:,1]+june_bruit[:,:,2])/3

    # Chargement de l'image paresseux et conversion en niveau de gris
    paresseux = img.imread('paresseux.png')
    paresseux = (paresseux[:,:,0]+paresseux[:,:,1]+paresseux[:,:,2])/3

    # Test des fonctions
    im0 = init(10)

    # Affichage des images
    plt.imshow(im0,plt.cm.gray)
    plt.show()