"""Напишите функцию, которая сортирует числовой список, не
используя никаких функций, вроде sort, sorted, max, min и т.д."""


sp = [1, 3, 2, 43, 65, 1, 993, 72, 0, 5, 52]

def sort(sp):
    for i in range(len(sp)):
      for k in range(len(sp)-i-1):
          print(sp)
          if sp[k] > sp[k+1]:
              sp[k], sp[k+1] = sp[k+1], sp[k]
    return sp
print(sort(sp))
