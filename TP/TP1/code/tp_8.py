#8;1
def calcul_impot_1(revenu):
    if revenu < 5875:
        impot = 0
    else:
        impot = (revenu-5875)*5.5/100
    print("Impots à payer", impot, " €")
calcul_impot_1(2000)

#8.2 8.3
def calcul_impot_2(revenu):
    if revenu < 5875:
        impot = 0
    elif revenu > 11720:
        impot = 14/100*revenu-1319.33
    else:
        impot = (revenu-5875)*5.5/100
    print("Impots à payer", impot, " €")
calcul_impot_2(50000)

#8.3 8.4
def calcul_impot_3(revenu):
    impot = 0
    if revenu < 11720:
        if revenu > 5875:
            impot = (revenu-5875)*5.5/100
    else :
        impot = 14/100*revenu-1319.33
    print("Impots à payer", impot, " €")
calcul_impot_3(25000)

#8.5
def calcul_impot_4(revenu):
    if revenu < 5875:
        impot = 0
    elif revenu >= 11720 and revenu < 26030:
        impot = 14/100*revenu-1319.33
    elif revenu >= 26030 and revenu < 69783:
        impot = 30/100*revenu-5484.13
    elif revenu > 69783:
        impot = revenu*40/100-12462.43
    else:
        impot = (revenu-5875)*5.5/100
    print("Impots à payer", impot, " €")
calcul_impot_4(25000)

#8.6
def calcul_impots_mars(revenu,cratere):
    impot = 0
    if revenu < 4800:
        if cratere:
            impot = 0.12*revenu
    else:
        if cratere:
            impot = 0.25*revenu-624
        else:
            impot = 0.12*revenu-576
    print("Impots à payer", impot, "€")
calcul_impots_mars(6000,False)
