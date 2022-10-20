#36.1
mat_test = [[10,7,3],[6,9,9],[7,5,7]]
def list_c(tab):
    list_colonne = []
    finito = []
    list_min_candidats = [0 for x in range(len(tab[0]))]
    for col in range(len(tab[0])):
        for ligne in range(len(tab)):
            list_colonne.append(tab[ligne][col])
            list_min_candidats[col] = min(list_colonne)
        list_colonne = []
    maximum = max(list_min_candidats)
    for i in range(len(list_min_candidats)):
        if int(list_min_candidats[i]) == maximum:
            print("gggggg")
            finito.append(i)
    return finito

print(list_c(mat_test))