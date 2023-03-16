# Tests

def mediane(sample):
    sample.sort()
    if len(sample)%2 == 0:
        return (sample[len(sample)//2 - 1] + sample[len(sample)//2])/2
    else:
        return sample[len(sample)//2]
    
a = [8, 2, 6, 4]
b = [1, 2, 5, 8, 11, 12]

print(mediane(a))