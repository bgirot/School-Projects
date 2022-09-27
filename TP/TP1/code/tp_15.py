#15.1

#15.2
def deplacement_possible(c1,c2):
    x1 = int(ord(c1[0]))
    y1 = int(c1[1])
    x2 = int(ord(c2[0]))
    y2 = int(c2[1])
    assert 65<=x1<=72 and 65<=x2<=72 and 1<=y1<=8 and 1<=y2<=8, ("Déplacement impossible, une case entrée n'existe pas")    #97 = ord('A') et 104 = ord('H') ne pas oublier les maj            
    if abs(x1-x2) == 1:
        if abs(y1-y2) == 2:
            print("Déplacement possible")
        else:print("Déplacement impossible")
    elif abs(y1-y2) == 1:
        if abs(x1-x2) == 2:
            print("Déplacement possible")
        else:
            print("Déplacement impossible")
    else : print("Déplacement impossible") 
#deplacement_possible("D4","C5")

def case_exist(c):
    xc1 = int(ord(c[0]))
    yc1 = int(c[1:])
    if 65<=xc1<=72 and 1<=yc1<=8:
        return 1
    else:
        return 0

def case_possible(c1):
    x1 = int(ord(c1[0]))
    y1 = int(c1[1])             #Pb quand y négatif, car le '-' est compté comme un caractère, donc on prend en compte tous les char sauf le premier
    assert 65<=x1<=72 and 1<=y1<=8, ("La case entrée n'existe pas")
    print("Cases possibles : ")

    possible_1 = chr(x1+1)+str(y1+2)
    possible_2 = chr(x1+1)+str(y1-2)
    possible_3 = chr(x1-1)+str(y1+2)
    possible_4 = chr(x1-1)+str(y1-2)
    possible_5 = chr(x1+2)+str(y1+1)
    possible_6 = chr(x1+2)+str(y1-1)
    possible_7 = chr(x1-2)+str(y1+1)
    possible_8 = chr(x1-2)+str(y1-1)

    if case_exist(possible_1) == 1 : print(possible_1)
    if case_exist(possible_2) == 1 : print(possible_2)
    if case_exist(possible_3) == 1 : print(possible_3)
    if case_exist(possible_4) == 1 : print(possible_4)
    if case_exist(possible_5) == 1 : print(possible_5)
    if case_exist(possible_6) == 1 : print(possible_6)
    if case_exist(possible_7) == 1 : print(possible_7)
    if case_exist(possible_8) == 1 : print(possible_8)

case_possible("D5")