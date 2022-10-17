def espace(chaine):
    for i in range(len(chaine)):
        if str(chaine[i]) == ' ':
            final = chaine[i+1:]            #split utilisable
    return final

def relou(li_corps):
    base = []
    finito = ""
    for i in range(len(li_corps)):
        base.append("De " + str(li_corps[i])+str(", ") + str(espace(li_corps[i]))+str(", ") + str(espace(li_corps[i])))
    return base
        

def jean(li_corps):
    for i in range(len(li_corps)):
        print("Jean Petit qui danse (bis)\nDe " + str(li_corps[i]) + str(" il danse (bis)"))
        for j in range(i+1,0,-1):
            print((relou(['son doigt','sa main','ses cheveux']))[j-1])
        print("Ainsi danse Jean Petit.\n")


jean(['son doigt','sa main','ses cheveux'])