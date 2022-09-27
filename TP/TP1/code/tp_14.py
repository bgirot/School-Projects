#14.1
"""
Si a1 ou a2 ou a3 mal transmis
Si b est bien transmis en br, alors br = a1+a2+a3, or une de ces trois valeurs a été modifiée en ar1 ou 
ar2 ou ar3, donc br !=ar1+ar2+ar3, de meme pour c dont seuls les coefficients changent
Pour corriger l'erreur : 
- on sait que br = b = a1+a2+a3
- on sait que cr = c = a1+2*a2+3*a3
- on a donc cr et br les valeurs réelles de c et b

on fait la somme des ar : ar1+ar2+ar3, et on observe la différence entre cette somme et b
on a donc s1 = (ar1+ar2+ar3)-(b). Si s1 > 0 : un a est + grand que prévu sinon un a est + petit que prévu

on fait de meme avec c : ar1+2*ar2+3*ar3, on observe la diff avec c
on a s2 = (ar1+2*ar2+3*ar3)-(c) : on a une différence entre c et cette somme
cette différence est forcément égale à k*s1, on sait donc quel coeeficient à été modifié :
si k = 1, a1 est erroné, si k = 2, a2 est erroné, si k = 3, a3 est erroné
"""

14.2
"""
14.2 : si c ou b mal transmis.
-  On sait que a1=ar1 a2 = ar2 et a3=ar3 donc on peu en déduire b et c, peut importe la valeur de cr et br
-  On observe ensuite la différence entre les expressions de b et c et b et cr, pour trouver la valeur
erronnée, et on la retrouve grâce à sa différence par rapport à la valeur réelle
"""

#14.3
def code_correcteur(ar1,ar2,ar3,br,cr):
    test_b = ar1+ar2+ar3
    test_c = ar1+2*ar2+3*ar3
    #Test validité c et b
    if br == test_b and not cr == test_c:
        print("c a mal été transmis : sa vraie valeur est : ",ar1+2*ar2+3*ar3)
    elif cr == test_c and not br == test_b:
        print("b a mal été transmis : sa vraie valeur est : ",ar1+ar2+ar3)
    #Test de validité de a1 a2 et a3 (b et c ont passé le test, ils ont donc été correctement transmis)
    else:
        s1 = test_b-br
        s2 = test_c-cr
        #Si les trois entier sont correctement transmis (en + de b et c)
        if s1 == s2 == 0:
            print("Les cinq entiers ont été correctement transmis")
        #Test de validité de chaque a en fct de sont coef dans c (calcul de la différence entre br, cr et b et r)
        else:
            if s1 == s2:
                print("a1 a mal été transmis : sa vraie valeur est : ",ar1-s1)
            elif s2 == 2*s1:
                print("a2 a mal été transmis : sa vraie valeur est : ",ar2-s1)
            elif s2 == 3*s1:
                print("a3 a mal été transmis : sa vraie valeur est : ",ar3-s1)
            else:
                print("erreur programme")

code_correcteur(3,2,6,10,25)