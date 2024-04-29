words = input().split(" ")
max_ = 0
index_ = 0
for i in words:
  if len(i) > max_:
    max_ = len(i)
    index_ = words.index(i)
for i in words:
  if len(i) == max_:
    print(i)