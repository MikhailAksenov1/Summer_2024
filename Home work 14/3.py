"""Напишите рекурсивную функцию tri_2(n), которая печатает два треугольника.
• Например, для n = 5:
• *****
• ****
• ***
• **
• *
• **
• ***
• ****
• *****
• Подсказка: одна строка печатается до вызова функции, а вторая после вызова"""

def tri_2(n):
  print('*'*n)
  if n > 1:
    tri_2(n - 1)
    print('*'*n)
tri_2(5)