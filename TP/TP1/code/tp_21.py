#21.1
def somme_1(n):
    somme = 0
    for k in range(1,n+1):
        somme += (k**2)/(k**2 + 1)
    return somme

#21.2
def somme_2(n):
    li_1 = []
    for i in range(1,n+1):
        li_1.append((n+i)/(n**2 + i**2))
    return li_1

#21.3
def somme_3(n):
    li_2 = []
    for k in range(1,n+1):
        print(somme_2(k))

#21.4
def somme_4(n):
    rep = 0
    for k in range(1,n+1):
        for i in range(1,k+1):
            rep += (k+i)/(k**2 + i**2)
    return rep
print(somme_4(5))