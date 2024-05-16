c = int(input())
f = [1,1]
for i in range(c):
  f.append(f[-1] + f[-2])
print(f)