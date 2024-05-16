t = int(input())
p = [1]
for i in range(t):
    c = []
    print(p)
    for i in range(len(p)-1):
      c.append(p[i] + p[i + 1])
    c.append(1)
    c.insert(0,1)
    p = c