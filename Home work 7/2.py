def cezar(n, str1):
    a = 'abcdefghijklmnopqrstuvwxyz'
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str2 = ''
    for i in str1:
        if i in a:
            index = a.index(i) + n
            if index >= len(a):
                index = index % len(a)
            str2 = str2 + a[index]
        if i in A:
            index = A.index(i) + n
            if index >= len(A):
                index = index % len(A)
            str2 = str2 + A[index]

    return str2
print(cezar(int(input()), input()))
