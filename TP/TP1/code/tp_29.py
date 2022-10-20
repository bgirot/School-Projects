dict_morse={
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    ' ':'  ',
}

def traduire_text_morse(dico,chaine):
    finito =''
    for i in range(len(chaine)):
        finito += str(dico.get(chaine[i]))
        finito += " "
    return finito
print(traduire_text_morse(dict_morse,"PEDRO"))

def reverse_dict(dico):
    reverse_dico = dict()
    for k,v in dico.items():
        reverse_dico[v] = k
    return reverse_dico

def traduire_morse_vers_texte(dico,chaine):
    finito = ''
    liste_mots = chaine.split(' ')
    #Sépare chaque mot puis change les doubles espaces (devenus '' à cause du split) en '  '
    for i in range(len(liste_mots)):
        if str(liste_mots[i]) == '':
            liste_mots[i] = "  "
    for el in liste_mots:
        finito += str(dico.get(el))
    return finito
print(traduire_morse_vers_texte(reverse_dict(dict_morse),".-.. .  -.-. .... .- -  . ... -  -. --- .. .-."))