#18
import time
t = time.time()
"""
Explication de la méthode :
On caractérise la grille par sa longueur et sa largeur
On caractérise chaque carré par son coin supérieur gauche et son coin inférieur droit
Pour dénombrer tous les rectangles possibles, on va étudier un par un chaque coin sup gauche et lui
associer toutes les possibilités de coin inf droit. 
On aura donc 2 grandes partie dans notre programme, chacune constituée de 2 boucles for :
les 2 premieres : renvoient les coord du coin sup gauche
les 2 suivantes : renvoient les coord du coin inf droit
On vérifie ensuite que le coin inférieur droit est bien inférieur(x1<=x2) et à est
à droite (y1<=y2), puis on le comptabilise dans les possibilités
Enfin pour répondre l'exercice on utiliser une boucle qui teste les possiblités et renvoie
celle qui se rapproche le plus de 2M
"""

##Méthode 1 (très lente et peu efficace car trop de boucles, fonctionne dans l'idée)
def nbr_rect_1(length,width):
    n = 0
    for x1 in range(1,length+1):
        for y1 in range(1,width+1):
            for x2 in range(1,length+1):
                for y2 in range(1,width+1):
                    if x1<=x2 and y1<=y2:
                        n+=1
    return n

##Méthode 2 (rapide)
def nbr_rect_2(length,width):
    n = (length * width * (width + 1) * (length + 1)) // 4
    return n

closer = 10**10
for x_grille in range(1,3000):
    for y_grille in range(1,3000):
        test = nbr_rect_2(x_grille,y_grille)
        if abs(2*10**6 - test) < abs(2*10**6-closer):
            closer = test
            closer_x = x_grille
            closer_y = y_grille

print("la grille dont le nombre de rect possibles est le plus proche de 2 millions a\n pour dimensions",closer_x,"x",closer_y,"avec",nbr_rect_2(closer_x,closer_y),"rectangles.")
print("Temps d'exécution : ",time.time()-t)