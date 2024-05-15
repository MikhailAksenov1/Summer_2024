arif = input().split(' ')
a = int(arif[0])
b = int(arif[2])
if arif[1] == '+':
    print(a + b)
if arif[1] == '-':
    print(a - b)
if arif[1] == '*':
    print(a * b)
if arif[1] == '/':
    print(a / b) if b != 0 else print('Деление на ноль')
