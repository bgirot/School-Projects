#10
def somme(n):
    k = 0
    s = 0
    while k < n:
        k += 1
        s += 1/k
    return s
print(somme(10))
"""
En remplaçant k<n par k<=n le prgm aurait calculé la somme des 1/k allant de 1 à n+1
"""
def h(n):
    k = 1
    s = 1
    while k < n:
        k += 1
        s *= 1-1/(k**2)
    return s
print(h(5))

def entier():
    n = 0
    s = 0
    while s < 10:
        n += 1
        s += 1/n
    print("Le plus petit entier tel que S(n)>=10 est", n)
entier()

def lim(epsilon):
    n = 2
    while not (0.5-epsilon <= h(n) and 0.5+epsilon >= h(n)):
        n +=1
    print("Le plus petit entier n tel que 0.5-e<=Hn<=0.5+e avec e =", epsilon, "est", n)
lim(0.002)