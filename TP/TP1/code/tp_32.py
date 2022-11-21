import math
import numpy as np

#1
"""
np.zeros(7)                             ---> affiche 7 zéros
np.ones(6)                              ---> affiche 6 uns
np.identity(3)                          ---> affiche la matrice identité de dimension 3x3
np.array([3,7,-1,2])                    ---> affiche la matrice ligne ...
np.array([[3,7],[-1,2]])                ---> affiche la matrice carrée ...
np.arange(10,30,5)                      ---> renvoie la liste des valeurs de 5 en 5 entre 10 et 30 exclus 
np.linspace(0,2,9)                      ---> renvoie 9 éléments régulièrement espacés entre 0 et 2
np.sin(np.linspace(0,2*np.pi,20))       ---> renvoie les sinus de 20 éléments régulièrement espacés entre 0 et 2pi
math.sin(np.linspace(0,2*np.pi,20))     ---> erreur car math.sin ne marche que sur des matrices 1x1
"""

#2
"""
a = np.array([[1,3],[0,4]])
b = np.array([[4,0],[-1,1]])
a+b                                     ---> additionne les coefficients entre eux dans une matrice de mm dimension
a+4                                     ---> ajoute 4 à chaque coefficient de la matrice a
a*b                                     ---> produit des matrices a et b
3*a                                     ---> multiplie par 3 chaque coef
np.add(a,b)                             ---> additionne les coeffs
a.dot(b)                                ---> produit vectoriel ??????
a @ b                                   ---> produit matriciel
a.transpose()                           ---> inverse l'ordre des coefs
np.linalg.matrix_power(a,2)             ---> élève la matrice au carré
a.shape                                 ---> donne les dimensions de la matrice
"""

#3
"""
a.sum()                                 ---> somme les coefs
a.sum(axis=0)                           ---> somme les coeff
...
"""

#4
