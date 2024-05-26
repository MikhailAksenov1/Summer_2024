def dnk_rnk(x):
    dnk = {'G':'C', 'C':'G', 'T':'A', 'A':'T'}
    x = list(x)
    for i in range(len(x)):
        for k in dnk.keys():
            if x[i] == k:
                x[i] = dnk[k]
                break
    return ''.join(x)


res = input().upper()
print(dnk_rnk(res))