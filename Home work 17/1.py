"""Напишите программу программу, которая устраняет повторение
повторение слов, т.е. результат результат должен быть следующим:
Напишите программу, которая устраняет повторение слов, т.е.
результат должен быть следующим."""

import re

text = 'Напишите напишите программу программу, которая которая устраняет устраняет повторение повторение слов слов'
print(re.sub(r'([ЁёА-я]+)\s\1', r'\1',text, flags=re.IGNORECASE))