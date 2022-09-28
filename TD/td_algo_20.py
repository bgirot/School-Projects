def pos(n,k):
    assert n>0 and k>0
    k -= 1
    if n == 1:
        return(0)
    else :
        li = [x for x in range(1,n)]                #Créé une liste des rangs des personnes
        elim = k%len(li)                            #Rang premier élminé après n = 0

        while len(li) > 1:                          #On élimine jusqu'à ce qu'il ne reste qu'1 survivant
            li.pop(elim)                            #Retire l'éliminé de la liste
            elim = (elim + k)%len(li)               #Ajoute k au rang du dernier éliminé, et ce modulo le nombre de survivant
        return li[0]

print("rang du dernier survivant :", pos(4,6))