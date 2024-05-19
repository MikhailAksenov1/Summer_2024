n = input()
dict1 = {'numbers':{}, 'special':{}, 'letters':{}}
for i in n:
    if i.isdigit():
        dict1['numbers'][i] = dict1['numbers'].get(i, 0) + 1
    elif i.isalpha():
        dict1['letters'][i] = dict1['letters'].get(i, 0) + 1
    else:
        dict1['special'][i] = dict1['special'].get(i, 0) + 1
for key in dict1:
    print(*dict1[key].keys())

