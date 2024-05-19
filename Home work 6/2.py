misha = input().split(',')
kolya = input().split(',')
books = {}
for i in misha:
    books[i] = books.get(i, 0) + 1
for i in kolya:
    books[i] = books.get(i, 0) + 1
print(len([k for k in books if books[k] == 2]))