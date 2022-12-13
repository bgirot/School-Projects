def doublon(tab):
    for i in range(len(tab)):
        for j in range(i-1):
            if tab[j] == tab[i]:
                return True
        for k in range(i+1,len(tab)):
            if tab[k] == tab[i]:
                return True
    return False

def doublon2(tab):
    for i in range(len(tab)):
        test = list(tab).pop(i)
        print(test)
print(doublon2([0,1,2,3]))