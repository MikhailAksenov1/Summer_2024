n = int(input())
n = str(n)
for i in range(10):
  print("{}-{}".format(i,n.count(str(i))))