a = input()
n = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
n2 = {'IV':4, 'IX':9, 'XC':90, 'XL':40, 'CD':400, 'CM':900}
sum = 0
for i in n2:
    if i in a:
        a = a.replace(i, '')
        sum += n2[i]
for i in a:
    sum += n[i]
print(sum)
