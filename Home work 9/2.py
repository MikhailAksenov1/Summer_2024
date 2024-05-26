def similar(x, k):
    lst = []
    lst1 = 'ауоиэыяюеё'
    x = x.lower()
    for i in x:
        if i in lst1:
            lst.append(x.index(i))
    lst2 = []
    for i in k:
        count = 0
        vo_count = 0
        for j in i:
            if j in lst1:
                vo_count += 1
        for d in lst:
            if i[d] in lst1:
                count += 1
        if count == vo_count and count == len(lst):
            lst2.append(i)
    return lst2


x = input().lower()
n = int(input())
k = []
for i in range(n):
    k.append(input().lower())
print(similar(x, k))


