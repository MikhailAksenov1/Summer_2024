text = input().lower()
d = {}
c = {}
new_sent = False
for i in text:
    if i not in ' ,.:;"01234567890':
        if not new_sent:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        else:
            if i not in c.keys():
                c[i] = 1
            else:
                c[i] += 1
    if i == '.': #если появляется второе новое предложение,то оно разделено "."
        new_sent = True
if c == d:
    print(True)
else:
    print(False)