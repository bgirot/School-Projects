def espace(chaine):
    for i in range(len(chaine)):
        if str(chaine[i]) == ' ':
            final = chaine[i+1:]            #split utilisable
    return final
print(espace('je suis'))

def jean(li_corps):
    for i in range(len(li_corps)):
        print("Jean Petit qui danse (bis)\nDe" + str(li_corps[i]) + str(" il danse (bis)\nDe ") + str(li_corps[i])+str(", ") + str(espace(li_corps[i]))+str(", ") + str(espace(li_corps[i])) + str("\nAinsi danse Jean Petit.\n"))


jean(['son doigt','sa main','ses cheveux'])