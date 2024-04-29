summa = 0
len_ = 0
while True:
    salaries = float(input())
    if salaries == 0:
        break
    summa += salaries
    len_ += 1
print(summa / len_)