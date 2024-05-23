def abab(x):
    sp = []
    for i in x:
        if i not in sp:
            sp.append(i)
    x1 = sorted(x, reverse=True)
    return len(sp), ord('z') - ord(x1[0].lower())


def ab(x):
    return sorted(x, key=abab)[::-1]


print(ab(['abab', 'xx', 'aaaa', 'bbbb', 'ccdf', 'acaca']))
