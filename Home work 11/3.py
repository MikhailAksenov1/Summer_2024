def arab_rim(x):
    n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XC': 90, 'XL': 40, 'CD': 400, 'CM': 900}
    sum = ''
    n = {k: v for k, v in sorted(n.items(), key=lambda item: item[1], reverse=True)}
    for b, k in n.items():
        while x >= k:
            sum += b
            x -= k
    return sum


while True:
    a = int(input())
    if a == 0:
        break
    print(arab_rim(a))



