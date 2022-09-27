
def gray(g_init):
    li1 = [i+[0] for i in g_init]
    li2 = [i+[1] for i in g_init]
    print(li1)
    print(li2)
    li2.reverse()
    g_final = li1+li2
    return g_final
print(gray([[0,0],[1,0],[1,1],[0,1]]))
