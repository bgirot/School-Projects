#CC 1 - ex 5
#5.1
"""
{1,4,5,7} est compris dans l'ensemble [0,7]
On peut donc le représenter par le tableau
de booléens suivant :
[False,True,False,False,True,True,False,True]
"""

#5.2
"""
Ce tableau représente l'ensemble :
{1,2,3,7}
"""

#5.3 a) (explcation en 5.4)
"""
La fonction renvoie le tableau :
[Faux,Faux,Faux,Vrai,Faux,Vrai]
"""

#5.3 b)
#Fonction traduite en python
def f(tab1,tab2):
    n = 0
    res = []
    for i in range(n-1):
        res[i] = tab1[i] and tab2[i]
    return res
"""
La fonction prend en paramètres 2 entiers et
retourne un tableau indiquant True si l'entier
est dans les deux tableaux au même rang et
sinon False
"""

#5.6 (5.4 normalement, erreur d'énoncé je pense)
def non_vide(ens):      #Fonction qui renvoie True si ens non vide, False si vide
    for el in ens:
        if el == True:
            return True
    return False
print(non_vide([False,False,False]))