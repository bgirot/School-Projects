import doctest
from time import *

def expo_normale(x,n):
    """
    >>> expo_normale(9,2)
    81
    """
    s = 1
    for i in range(n):
        s *= x
    return s

def expo_rapide(x,n):
    """
    >>> expo_normale(9,2)
    81
    """
    if n == 0:
        return 1
    elif n%2 == 0:
        a = expo_rapide(x, n//2)
        return a*a
    else:
        a = expo_rapide(x, (n-1)//2)
        return a*a*x
    


if __name__ == '__main__':
    doctest.testmod(verbose=True)