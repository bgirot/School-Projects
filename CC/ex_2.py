#CC 1 - ex 2
rep = int(input("Entrez un entier : "))
s = 0
i = 0

while rep != -1:
    s += rep
    i += 1
    rep = int(input("Entrez un entier : "))

moy = s/i 
print(moy)

"""
Il y a d'autres moyens de le faire, avec une boucle 
for et une condition (if rep == -1) par exemple
"""