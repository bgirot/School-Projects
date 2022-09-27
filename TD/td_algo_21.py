from time import time
start = time()
length = 2357207
n = 28433*(2**7830457)+1
deci = n%(10**10)
print("10 dernières décimales :", deci,"\nTemps d'exécution : ", time()-start)