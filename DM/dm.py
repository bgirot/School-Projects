import matplotlib.pyplot as plt
import matplotlib.image as img

def neg(im) :
    return [1-y for y in [x for x in im]]

def miroir(im) :
    return [x[::-1] for x in im]

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
    photomaton_matrix = im.copy()
    n = len(im)//2

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
    if k == 1 :
        return photomaton(im)
    else:
        return photomaton(mlgk(im, k-1))

# Réduction du nombre de couleurs
def f(x, b) :
    deux_b = 2**b
    return int(deux_b * int(255*x)/256)/(deux_b-1)

def moins_de_coul(im, b) :
    return [[f(y, b) for y in x] for x in im]

def moins_de_pix(im, k) :
    moins_de_pix_matrix = [[0 for y in range(len(im)//k)] for x in range(len(im)//k)]
    for i in range(len(im)):
        for j in range(len(im)):
            if i%2 == 0 and j%2 ==0:
                moins_de_pix_matrix[i//k][j//k] = im[i][j]
    return moins_de_pix_matrix

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
    plt.imshow(mlgk(june, 8),plt.cm.gray)
    plt.show()
