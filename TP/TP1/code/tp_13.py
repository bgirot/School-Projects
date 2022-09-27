s = 0
for k in range(1,1000):
    if k%5 == 0 or k%3 == 0:
        s += k
print("Somme :", s)