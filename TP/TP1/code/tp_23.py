#23.1
def fct_1(n):
    k = 2
    while n%k != 0:
        k += 1
    return k

#23.2
def fct_2(n):
    k = n-1
    while n%k != 0:
        k -= 1
    return k

#23.3
def fct_3(n,p):
    k = 2
    while not (n%k == 0 and p%k ==0):
        k += 1
    return k

#23.4
def fct_4(n,p):
    k = 2
    while not (n%k == 0 and p%k ==0) and k<=n:
        k += 1
    if k == n+1:
        print(n,"et",p,"sont premiers entre eux")
    else:
        print("PPCD ",n,"et",p,":",k)
    return k

#23.5
def fct_5(n):
    div = []
    for i in range(1,n+1):
        if n%i == 0 :   div.append(i)
    return div

#23.6
def fct_6(n):
    somme = 0
    for i in range(len(fct_5(n))):
        somme += fct_5(n)[i]
    return somme

#23.7
def parfait(n):
    if n == fct_6(n)-n:
        return 1
    else:
        return 0

#23.8
def liste_parfait(n,p):
    liste = []
    for i in range(n,p+1):
        if parfait(i) == 1:
            liste.append(i)
    return liste
print(liste_parfait(2,40))