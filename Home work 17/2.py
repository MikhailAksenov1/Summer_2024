"""Создайте декоратор, которые переводит все текстовые аргументы функции в
верхний регистр и возвращает их в виде списка текстовых аргументов.
Текстовые аргументы – это строки в args и строковые значения в kwargs.
Например, если декорируемая функция вызывается с аргументами:
f(1, '2xyz', a= 3, b='4'),
то возвращаемый ею результат должен быть '2xyz4'"""


def args_upper(fu):
    def wrapper(*args, **kwargs):
        sp = []
        for i in args:
            if type(i) == str: sp.append(i.upper())
        for k, v in kwargs.items():
            if type(v) == str: sp.append(v.upper())
        fu(sp)

    return wrapper


@args_upper
def fu(*args, **kwargs):
    print(*args)


fu(1, '2xyz', a=3, b='4')
