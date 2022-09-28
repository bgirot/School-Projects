#24.1
personne_1 = [x for x in range(1,9)]
parent_1 = [-1,6,8,0,8,7,0,6,6]
def premiere_generation(p,i):
    if p[i] == 0:
        return True
    else:
        return False

#24.2
def nbr_enfant(i):
    somme = 0
    for x in parent_1:
        if i == x:
            somme += 1
    return somme
