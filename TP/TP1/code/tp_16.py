#16
def binomial(n,k):
    coef = 1
    for i in range(1,k+1):
        print("k = ",i,"\nn = ",n)
        coef = (n-k+i)/(i)*coef
    return int(coef)
print(binomial(15,10))

#16 alts
#16.1
from math import comb
comb(15,10)

#16.2
from math import factorial
"on sait que k parmi n vaut n!/(k!*(n-k)!)"
def alt_binomial(n,k):
    coef_alt = factorial(n)/(factorial(k)*factorial(n-k))
    return int(coef_alt)