import math
def simul(n):
    bact = 1
    t = 0
    while n != 0:
        t += bact*(math.exp(-t)*(t+1))
        bact += 1
        n -= 1
    return(t)
rep = int(simul(5000))
print(rep)