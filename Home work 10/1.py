f = open('test1.txt', 'r', encoding='utf-8')
s = f.readlines()
f.close()
s = s[::-1]
t = open('test2.txt', 'w', encoding='utf-8')
for i in s:
    i = i.strip()
    i = i.split(' ')[::-1]
    i = ' '.join(i) + '\n'
    t.write(i)
t.close()
