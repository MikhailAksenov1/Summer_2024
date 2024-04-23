x = float(input())
y = float(input())
max_num = -10000
if x + y >= max_num:
  max_num = x + y
if x - y >= max_num:
  max_num = x - y
if x * y >= max_num:
  max_num = x * y
if y!=0:
  if x / y >= max_num:
    max_num = x / y
  if x // y >= max_num:
    max_num = x // y
print(max_num)
