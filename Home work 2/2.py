lst = [1, -3, 456, 0, -129]
m = lst[0]
for i in lst:
  if i < m:
    m = i
print(m)