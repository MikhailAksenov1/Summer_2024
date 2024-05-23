def agct(x):
    str2 = ''
    x = list(x)
    for i in range(len(x)):
        if x[i] == 'A' and i + 1 != len(x) and x[i + 1] == 'Г' or x[i] == 'Г' and i + 1 != len(x) and x[i + 1] == 'А':
            tmp = x[i]
            x[i] = x[i + 1]
            x[i + 1] = tmp
        elif x[i] == 'Ц' and i + 1 != len(x) and x[i + 1] == 'Т' or x[i] == 'Т' and i + 1 != len(x) and x[i + 1] == 'Ц':
            str2 += x[i] + 'АГ'
        else:
            str2 += str(x[i])
    return str2


print(agct(input().upper()))