def fta(x):
    x.lower()
    sl = {}
    for i in x:
        sl[i] = sl.get(i, 0) + 1
    sort_res = sorted(sl.items(), key=lambda item:(-item[1], item[0]))

    for i in sort_res[0:10]:
        print('{} - {}'.format(i[0], i[1]))


(fta(input()))