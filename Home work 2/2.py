lst = [1, -3, 456, 0, -129]
m = float("inf")
for i in lst:
  if i < m:
    m = i
print(m)