"""Напишите функцию, которая сравнивает две строки и выдает True,
если между ними есть не более, чем 1 разница в буквах, и False во
всех остальных случаях. Если две строки равны, то True.
Например:
‘abc’ и ‘abc’ – True, ‘abc’ и ‘abcd’ – True,
‘bc’ и ‘abc’ – True, ‘axc’ и ‘abc’ – True
‘abc’ и ‘acb’ – False, ‘abc’ и ‘a’ – False, ‘’ и ‘ ‘ - False"""


def true_false(st1, st2):
    if len(st1) == len(st2):
        count = 0
        for i in range(len(st1)):
            if st1[i] != st2[i]:
                count += 1
            if count > 1:
                return False
        if count <= 1:
            return True
    elif len(st1) - len(st2) == 1 or len(st2) - len(st1) == 1:
        if st1 in st2:
            return True
        elif st2 in st1:
            return True
        else:
            return False

    else:
        return False


print(true_false(input(), input()))
