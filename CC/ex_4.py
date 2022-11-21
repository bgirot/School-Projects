#CC 1 - ex 4
def carres(tab):
    liste_carres = []
    for el in tab:
        liste_carres.append(el**2)
    return liste_carres
print(carres([3,5,7,9]))