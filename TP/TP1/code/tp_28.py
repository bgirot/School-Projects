#28
def occurences_lettre(chaine):
    dico = dict()
    for letter in chaine:
        dico[letter] = 0
    for letter in chaine:
        dico[letter] = dico.get(letter)+1
    return dico
print(occurences_lettre("Zoo"))

def frequences_lettres(chaine):
    dico2 = dict()
    for letter in chaine:
        dico2[letter] = 0
    for letter in chaine:
        dico2[letter] = dico2.get(letter)+1
    for letter in dico2:
        dico2[letter] = dico2[letter]/len(chaine)
    return dico2
print(frequences_lettres("Zoo"))