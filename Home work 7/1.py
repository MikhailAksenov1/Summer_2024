def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    s = a + b
    return s


def nok(n):
    for i in range(len(n)):
        if i == 0:
            s2 = nod(n[i], n[i+1])
            s3 = n[i+1]*n[i]//s2
        else:
            s = s3
            s2 = nod(s, n[i])
            s3 = s*n[i]//s2
    return s3


print(nok([4, 6, 8, 16, 2]))
