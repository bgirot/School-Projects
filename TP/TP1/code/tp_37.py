import doctest
def triangle_haut(n):
    if n > 0:
        triangle_haut(n-1)
        print(n * "*")

def triangle_bas(n):
    """
    Test :
    >>> triangle_bas(5)
    *****
    ****
    ***
    **
    *
    """
    print(n*"*")
    if n > 1:
        triangle_bas(n-1)

def sablier(n):
    """
    >>> sablier(4)
    ****
    ***
    **
    *
    **
    ***
    ****
    """
    print(n*"*")
    if n>1:
        sablier(n-1)
        print(n*"*")

def triangle_milieu(n):
    if n > 1:
        triangle_milieu(n-1)
        print(n*"*")
        triangle_milieu(n-1)
triangle_milieu(5)

#if __name__ == '__main__':
#    doctest.testmod(verbose=True)
