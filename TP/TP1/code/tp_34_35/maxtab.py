def maxtab(tab):
    """
    commentaire
    """
    m = tab[0]
    for el in tab[1:]:
        if el>m:
            m = el
    return m