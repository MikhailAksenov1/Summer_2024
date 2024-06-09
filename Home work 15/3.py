"""Напишите функцию, которая находит в строке все телефонные номера,
которые удовлетворяют следующим шаблонам:
+7(812)DDD-DDDD, +7(812)DDD-DD-DD, +7(921)DDD-DDDD, +7(921)DDD-DD-DD
где D любая цифра"""

import re
def find_num(st):
    n = r"\+7\(812\)\d{3}-\d{4}\b|\+7\(921\)\d{3}-\d{4}\b|\+7\(812\)\d{3}-\d{2}-\d{2}\b|\+7\(921\)\d{3}-\d{2}-\d{2}\b"
    return re.findall(n, st)
print(*find_num('efoejrfijeo  .+7+7(921)111-0101, +7(812)666-74113 +7(812)666-7411 AA777BA78 +7(921)K786KH178wjf +7(921)111-01-88 owijfowjfw owcmwlmkcopcwpowopefkm +7(812)123-12-12 efjeoifje '))