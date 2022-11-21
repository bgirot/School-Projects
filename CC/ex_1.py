#CC 1 - ex 1
def ex1(n):
    s = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            s += (i*j)/(i+j)
    return s
print(ex1(3))

#vérifiable sur https://www.dcode.fr/calcul-sommation"