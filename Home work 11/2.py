from openpyxl import Workbook

f = open('test5.txt', 'r', encoding='utf-8')
s1 = f.readlines()
s2 = []
for i in s1:
    s2.append(i.split(','))
s2.sort(key=lambda fs: (fs[3], fs[1], fs[2]))
f.close()


wb = Workbook()
str_active = wb.active
su = 0
for i in s2:
    str_active.append({1:i[0], 2:i[1], 3:i[2], 4:i[3], 5:i[4]})
    su += int(i[4])
str_active.append({1:'ИТОГО:', 5:su})

wb.save('test5_1.xlsx')
print(s2)