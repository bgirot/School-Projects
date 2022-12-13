def calcule_moyenne(f):
    d = {}
    infos = [el.split(";") for el in f.read().split("\n")]
    for el in infos:
        d[el[0]] = sum([float(elem) for elem in el[1:]])/4
    return d

def exporte_moyenne(dico,fichier_cible):
    for key,value in dico.items():
        fichier_cible.write(str(key),";",str(value[0]),";",str(value[1]),";",str(value[2]),";",str(value[3]))
exporte_moyenne(calcule_moyenne(open("notes_etudiants.csv",'r')),open("fichier_cible.csv","w"))