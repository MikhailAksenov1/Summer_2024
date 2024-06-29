"""Найдите длину наибольшей подстроки данной строки, которая
является палиндромом.
Например, дана строка ‘aabbccddcc’ тогда длиной подстроки с
наибольшим палиндромом является 6 (подстрока ‘ccddcc’)"""

s = 'aaaaabbbccddccc'


def polindrom(x):
    max_len = (0, 0)
    for i in range(len(x)):
        start, end = valid(i - 1, i)
        if max_len[1] - max_len[0] < end - start:
            max_len = (start, end)
        start, end = valid(i, i)
        if max_len[1] - max_len[0] < end - start:
            max_len = (start, end)

    return (s[max_len[0]:max_len[1] + 1])


def valid(index_left, index_right):
    while index_left >= 0 and index_right < len(s) and s[index_left] == s[index_right]:
        index_left -= 1
        index_right += 1
    return index_left + 1, index_right - 1


print(polindrom(s))
