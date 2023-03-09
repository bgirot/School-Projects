import matplotlib.pyplot as plt
import matplotlib.image as img

def neg(im) :
    neg_matrix = [[1 for x in range(len(im[0]))] for y in range(len(im))]
    for i in range(len(im)):
        for j in range(len(im[0])):
            neg_matrix[i][j] -= im[i][j]
    return neg_matrix

def miroir(im) :
    mirror_matrix = [[0 for x in range(len(im[0]))] for y in range(len(im))]
    for i in range(len(im)):
        for j in range(len(im[0])):
            mirror_matrix[i][len(im[0]) - j - 1] = im[i][j]
    return mirror_matrix

def plus_de_lumiere(im,d) :
    lum_matrix = [[0 for x in range(len(im[0]))] for y in range(len(im))]
    for i in range(len(im)):
        for j in range(len(im[0])):
            current_pixel = im[i][j]
            if current_pixel + d > 1:
                lum_matrix[i][j] = 1
            elif current_pixel + d < 0:
                lum_matrix[i][j] = 0
            else:
                lum_matrix[i][j] = current_pixel + d
    return lum_matrix

def plus_de_contraste(im,k) :
    ctrst_matrix = [[0 for x in range(len(im[0]))] for y in range(len(im))]
    for i in range(len(im)):
        for j in range(len(im[0])):
            current_pixel = im[i][j]
            if current_pixel + k*(current_pixel-0.5) > 1:
                ctrst_matrix[i][j] = 1
            elif current_pixel + k*(current_pixel-0.5) < 0:
                ctrst_matrix[i][j] = 0
            else:
                ctrst_matrix[i][j] = current_pixel + k*(current_pixel-0.5)
    return ctrst_matrix

def photomaton(im) :
    photo_matrix = [[0 for x in range(len(im[0])*2)] for y in range(len(im)*2)]
    for i in range(len(photo_matrix)):
        for j in range(len(photo_matrix[0])):
            photo_matrix[i][j] = im[int(i%(len(photo_matrix)/2))][int(j%(len(photo_matrix[0])/2))]
    return photo_matrix

def mlgk(im, k) :
    if k == 0:
        return photomaton(im)
    else:
        print(k)
        return photomaton(mlgk(im, k-2))

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
    plt.imshow(mlgk(june, 4),plt.cm.gray)
    plt.show()
