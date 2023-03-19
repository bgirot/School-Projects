from random import randint

def test(n):
    return (2*n+1)**2

even = 0
odd = 0

for i in range(100):
    x = randint(0, 100)
    if test(x) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Pairs :", even)
print("Impairs :", odd)