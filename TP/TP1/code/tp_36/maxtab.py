def maxtab(tab):
    """
    Returns the maximum value of a list
    Argument :
    - tab : the list whose maximum will be determined
    """
    m = tab[0]
    for el in tab[1:]:
        if el > m:
            m = el
    return m
