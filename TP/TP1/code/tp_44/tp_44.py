import matplotlib.pyplot as plt
def draw(points):
    liste_pts = points.read().split('\n')
    points.close()
    liste_coord = [el.split(" ") for el in liste_pts]
    plt.plot([float(el[0]) for el in liste_coord], [float(el[1]) for el in liste_coord])
    plt.show()
draw(open("points.dat",'r'))