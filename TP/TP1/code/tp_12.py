#12
def fct_1(k,n):
    for i in range(1,n+1):
        print("L'équipe", k, "se déplace contre l'équipe", i)


def fct_2(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("L'équipe", i, "se déplace contre l'équipe", j)
        print("")


def fct_3(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                pass
            else : 
                print("L'équipe", i, "se déplace contre l'équipe", j)
        print("")


def fct_4(n):
    for i in range(1,n+1):
        print("Matchs de l'équipe", i)
        for j in range(1,i+1):
            if i == j:
                pass
            else:
                print("L'équipe",i, "joue contre l'équipe", j)
        print("")
fct_4(4)
