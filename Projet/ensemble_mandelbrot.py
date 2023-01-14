import matplotlib.pyplot as plt
import numpy as np
import doctest

color_table = [
    (66, 30, 15),
    (25, 7, 26),
    (9, 1, 47),
    (4, 4, 73),
    (0, 7, 100),
    (12, 44, 138),
    (24, 82, 177),
    (57, 125, 209),
    (134, 181, 229),
    (211, 236, 248),
    (241, 233, 191),
    (248, 201, 95),
    (255, 170, 0),
    (204, 128, 0),
    (153, 87, 0),
    (106, 52, 3)]

def prochains_termes(x,y,a,b) :
    """
        Étant donnés x et y les premiers termes respectifs de deux suites définies dans la fonction, ainsi que
        a et b des paramètres naturels, renvoie les termes suivants des deux suites

        :param x: premier terme de la suite 1
        :param y: premier terme de la suite 2
        :param a: paramètre 1
        :param b: paramètre 2
        :type x: int
        :type y: int
        :type a: int
        :type b: int
        :return: les termes suivants des deux suites
        :rtype: tuple

        :Example:

        >>> prochains_termes(3,4,1,2)
        (-6, 26)
        >>> prochains_termes(0.5,0.1,1,3)
        (1.24, 3.1)
    """
    return x**2-y**2+a, 2*x*y+b

def indice_divergence(x,y,a,b,n) :
    """
        Étant donnés x,y,a,b définis dans prochains_termes(x,y,a,b) et n le terme initial de la suite, renvoie
        l'indice de divergeance de l'ensemble de Mandelbrot défini tq E = x**2+y**2

        :param x: premier terme de la suite 1 (0)
        :param y: premier terme de la suite 2 (0)
        :param a: paramètre 1
        :param b: paramètre 2
        :param n: rang initial de la suite (0)
        :type x: int
        :type y: int
        :type a: int
        :type b: int
        :return: l'indicde de divergeance de l'ensemble de Mandelbrot
        :rtype: n

        :Example:

        >>> indice_divergence(0,0,0.5,0.5,0)
        5
        >>> indice_divergence(0,0,0.01,0.1,0)
        -1
        >>> indice_divergence(0,0,-0.24,-0.9,0)
        8
    """
    if n > 127:
        return -1
    elif x**2 + y**2 > 4:
        return n
    else:
        next_x, next_y = prochains_termes(x,y,a,b)
        return indice_divergence(next_x,next_y,a,b,n+1)

def get_color(a,b) :
    """
        Étant donnés a et b les paramètres d'un ensemble de Mandelbrot, renvoie la couleur du pixel à associer
        à cet ensemble

        :param a: paramètre 1
        :param b: paramètre 2
        :type a: int
        :type b: int
        :return: la couleur en système RGB à afficher pour cet ensemble
        :rtype: tuple

        :Example:
        
        >>> get_color(0.01,0.1)
        (0, 0, 0)
        >>> get_color(-0.24,-0.9)
        (134, 181, 229)
    """

    n = indice_divergence(0,0,a,b,0)
    if n == -1:
        return (0,0,0)
    else:
        return color_table[n%len(color_table)]

def create_image(x,y,l,h,nb_px,nb_py) :
    res = np.zeros((nb_px, nb_py, 3), dtype=np.uint8)
    for i in range(nb_px) :
        for j in range(nb_py) :
            res[i][j] = get_color(x+i*l/nb_px,y+j*h/nb_py)
    return res

if __name__ == "__main__":
    doctest.testmod()
    img = create_image(-2.,-1.25,2.5,2.5,500,500)
    # img = create_image(-0.7,0.5,0.3,0.3,500,500)
    # img = create_image(-0.58,0.626,0.03,0.03,500,500)

    plt.imshow(img)
    plt.axis("equal")
    plt.axis('off')
    plt.show()