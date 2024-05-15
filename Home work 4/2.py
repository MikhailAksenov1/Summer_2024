n = int(input())
d = {}
i = 1
number = 1
mass = []
for i in range(n):
    arr = []
    for k in range(n):
        arr.append(0)
    mass.append(arr)

j = 0
k = 1
while number <= n * n:
    for i in range(n):
        if (j, i) not in d.keys():
            d[j, i] = number
            number += 1
    for i in range(1, n):
        if (i, n - k) not in d.keys():
            d[i, n - k] = number
            number += 1
    for i in reversed(range(n - 1)):
        if (n - k, i) not in d.keys():
            d[n - k, i] = number
            number += 1
    for i in reversed(range(n - 1)):
        if (i, j) not in d.keys():
            d[i, j] = number
            number += 1
    j+=1
    k+=1
for i in d.keys():
    mass[i[0]][i[1]] = d[i]

for i in range(len(mass)):
    for j in range(len(mass[i])):
        print(mass[i][j], end=' ')
    print()