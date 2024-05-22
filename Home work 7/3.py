def fmax(mass):
    maxes = [a for b in mass for a in b]
    maxes.sort()
    return maxes[-3:]


print(fmax([[1, 6, 3], [4, 5, 4]]))