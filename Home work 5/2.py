s = int(input())
d = []
for i in range(1, s + 1):
  if s % i == 0:
    d.append(i)
print(d)