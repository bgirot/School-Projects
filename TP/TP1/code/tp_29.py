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
    ' ':'␣',
}

def traduire_text_morse(dico,chaine):
    finito =''
    for i in range(len(chaine)):
        finito += str(dico.get(chaine[i]))
        finito += str("␣")
    return finito
print(traduire_text_morse(dict_morse,"LE CHAT EST NOIR"))

def reverse_dict(dico):
    reverse_dico = dict()
    for k,v in dico.items():
        reverse_dico[v] = k
    return reverse_dico

def traduire_morse_vers_texte(dico,chaine):
    finito = ''
    word = ''
    for i in range(len(chaine)):
        pass                                    #Erreur pcq chaque lettre en morse fait plusieurs caractères
    return finito
print(traduire_morse_vers_texte(reverse_dict(dict_morse),".-.. . -.-. .... .- - . ... - -.--- .. .-. "))