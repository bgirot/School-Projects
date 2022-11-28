import doctest

def maxtab(tab):
    """
    Returns the maximum value of a list
    Argument :
    - tab : the list whose maximum will be determined

    Tests :
    >>> maxtab([8,2,6])
    8
    """
    m = tab[0]
    for el in tab[1:]:
        if el > m:
            m = el
    return m
if __name__=='__main__':
    doctest.testmod(verbose=True)