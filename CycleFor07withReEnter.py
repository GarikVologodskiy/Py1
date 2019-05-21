a, b, c, d = [int(input()) for i in range(4)]

# a,b,c,d - checking
if (not (0 <= a <= 10) or (a > b)):
    while ((a < 0) or (a > 10) or (a > b)):
        print('Некорректное число a. Введите заново:')
        a = int(input())
if (not (0 <= b <= 10)):
    while ((b < 0) or (b > 10) or (a > b)):
        print('Некорректное число b. Введите заново:')
        b = int(input())
if (not (0 <= c <= 10) or (c > d)):
    while ((c < 0) or (c > 10) or (c > d)):
        print('Некорректное число c. Введите заново:')
        c = int(input())
if (not (0 <= d <= 10)):
    while ((d < 0) or (d > 10) or (c > d)):
        print('Некорректное число d. Введите заново:')
        d = int(input())

# print multiplication table
for i in range(a-1, b+1):
    for j in range(c, d+1):
        if i == (a-1):
            print('', j, sep='\t', end='')
        else:
            if j == c:
                print(i, '\t', sep='', end='')
            print(i*j, '\t', sep='', end='')
    print()

