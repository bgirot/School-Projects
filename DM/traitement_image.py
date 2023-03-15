import matplotlib.pyplot as plt
import matplotlib.image as img

def neg(im) :
    return [1-y for y in [x for x in im]]       # On applique 1-x à la valeur chaque pixel

def miroir(im) :
    return [x[::-1] for x in im]                # On inverse l'ordre des pixels de chaque ligne

def plus_de_lumiere(im,d) :
    return [[max(0, min(1, y+d)) for y in x] for x in im]   # Ajoute d (une certaine lum) mais garde les valeurs entre 0 et 1

def plus_de_contraste(im,k) :
    return [[max(0, min(1, y+k*(y-0.5))) for y in x] for x in im]   # Applique la fonction x + k*(x-0.5) 

def photomaton(im) :
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

    return [[im[2*i][2*j] if i < n and j < n else im[2*i][2*(j-n)+1] if i < n and j >= n else im[2*(i-n)+1][2*j] if i >= n and j < n else im[2*(i-n)+1][2*(j-n)+1] for j in range(2*n)] for i in range(2*n)]

def mlgk(im, k) :
    # Fonction récursive qui applique k fois la fonction photomaton à l'image
    return photomaton(im) if k == 1 else photomaton(mlgk(im, k-1))

# Réduction du nombre de couleurs
def f(x, b) :
    deux_b = 2**b
    return int(deux_b * int(255*x)/256)/(deux_b-1)

def moins_de_coul(im, b) :
    # On applique la fonction fb à chaque pixel de l'image
    return [[f(y, b) for y in x] for x in im]

def moins_de_pix(im, k) :
    # On parcourt l'image et on ne garde que les pixels dont l'indice est un multiple de k
    return [[im[i][j] for j in range(0, len(im), k)] for i in range(0, len(im), k)]

def moins_de_pix2(im, k) :
    matrix = [[0 for y in range(len(im)//k)] for x in range(len(im)//k)]

    for i in range(0, len(im)-k+1, k):
        for j in range(0, len(im)-k+1, k):
            average_block = 0
            for x in range(k):
                for y in range(k):
                    average_block += im[i+x][j+y]
            matrix[i//k][j//k] = average_block
            
    return matrix

def filtre_median(im, q) :
    return []

def init(k) :
    return []

def arbre_to_image(qt,i,j,k,im) :
    pass

def new_coul(x,nbc) :
    return 0

def test(im, i, j, k, nbc) :
    return False,-1

def image_to_arbre(im, i, j, k, nbc) :
    return 0

def taille(qt) :
    return 0

if __name__ == "__main__" :
    june = img.imread('june.png')
    june = (june[:,:,0]+june[:,:,1]+june[:,:,2])/3

    # plt.subplot(1,2,1)
    plt.imshow(moins_de_pix(june,9),plt.cm.gray)

    # plt.subplot(1,2,2)
    # plt.imshow(moins_de_pix2(june,9),plt.cm.gray)

    plt.show()
