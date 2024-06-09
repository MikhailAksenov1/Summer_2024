"""Напишите функцию, которая принимает строку символов, и
печатает все содержащиеся в ней номера автомашин по
следующему правилу:
LDDDLL78 или LDDDLL178,
где L – буквы, совпадающие по начертанию в русском и латинском
алфавите, D – цифры от 0 до 9.
Например, A123BC78 или X666XX178"""


import re
def auto_number(st):
    n = r"[ABEKMHOPCTXY]\d{3}[ABEKMHOPCTXY]{2}78|[ABEKMHOPCTXY]\d{3}[ABEKMHOPCTXY]{2}178"
    return re.findall(n, st)
print(*auto_number('efoejrfijeo +7(921)111-0101, AA777BA78+7(921)K786KH178wjf+7(921)111-0104owijfowjfw owcmwlmkcopcwpowopefkm +7(812)123-12-12 efjeoifje '))
