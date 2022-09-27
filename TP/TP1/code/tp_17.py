#17
tn = [(x*(x+1))/2 for x in range(286,1000000)]
pn = [(x*(3*x-1))/2 for x in range(166,1000000)]
hn = [x*(2*x-1) for x in range(144,1000000)]
common = list((set(tn).intersection(pn)).intersection(hn))

print(common[0],"est à la fois triangulaire pentagonal et hexagonal")