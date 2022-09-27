#2.1
def g(x):
    if x<0:
        return(-(x**2))
    else : 
        return(x**2)
print(g(-4))


#2.2
for i in range(5,10):
    print(i)
for i in range(6):
    print(i)
for i in range(30,3,-8):
    print(i)

#2.3
def h(x):
    assert x>0 and x==int(x)
    for i in range(0,x+1):
        if i%7 == 0:
            print(i, "est un multiple de 7")
print(h(39))
