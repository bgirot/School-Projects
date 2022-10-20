#19 bis

def somme_tab(li):
    s = 0
    for el in li:
        s += el
    return s

def produit_tab(li):
    s = 1
    for el in li:
        s *= el
    return s

def maximum(li):
    max = li[0]
    for el in li[1:]:
        if el>max:
            max = el
    return max

def indice_maximum(li):
    max = li[0]
    rang = 0
    rang_max = 0
    for el in li[1:]:
        rang += 1
        if el>max:
               max = el
               rang_max = rang
    return rang_max

def maximum_tab(li_1,li_2):
    li_final = []
    for i in range(len(li_1)):
        if li_1[i]>li_2[i]:
            li_final.append(li_1[i])
        else:
            li_final.append(li_2[i])
    return li_final
print(maximum_tab([1,4,5,6],[7,1,2,8]))