#11

def u(n):
    u = 0
    while n > 0:
        n -= 1
        u = (6+u)/(6-u)
    return u
print(u(5))
"""
Si on avait remplacé n>0 par n>= 0, le prgm aurait calculé un+2
Si on avait mis le test n < 0, la condition de la boucle n'aurait pas été validée dès le premier test, car n est un entier naturel
"""

def somme_un(n):
    k = 0
    s = 0
    while k <= n:
        s += u(k)
        k += 1
    print("Somme des Uk pour k allant de 0 à", n, "=", s)
somme_un(5)
