def sorting1(x):
    res = ''.join(str(i) for i in x)
    return len(res)


def sorting2(x):
    x.sort(key=sorting1)
    for i in x:
        i.sort(reverse=True)
    return x


print(sorting2([[1, 2, 3], [2, 44, 1, 4], [3, 3]]))
