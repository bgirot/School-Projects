#CC 1 - ex 3
def ex3(tab):
    notes_inf_8 = 0
    notes_entre_8_12 = 0
    notes_supp_12 = 0
    for el in tab:
        if el < 8:
            notes_inf_8 += 1
        elif el >= 8 and el <= 12:
            notes_entre_8_12 += 1
        else:
            notes_supp_12 += 1
    print("Il y a ",notes_inf_8,"notes <8, ",notes_entre_8_12," notes entre 8 et 12 et ",notes_supp_12)

ex3([5,6,6,8,10,11,12,16,20])