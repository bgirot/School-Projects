import matplotlib.pyplot as plt
import matplotlib.image as img
import doctest

def neg(im) :
    for el in im:
        print(el)

def miroir(im) :
    return []

def plus_de_lumiere(im,d) :
    return []

def plus_de_contraste(im,k) :
    return []

def photomaton(im) :
    return []

def mlgk(im, k) :
    return []

# Réduction du nombre de couleurs
def f(x, b) :
    deux_b = 2**b
    return int(deux_b * int(255*x)/256)/(deux_b-1)

def moins_de_coul(im, b) :
    return []

def moins_de_pix(im, k) :
    return []

def moins_de_pix2(im, k) :
    return []

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
    neg(june)
    plt.imshow(june,plt.cm.gray)
    plt.show()
