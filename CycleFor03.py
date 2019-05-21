a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d + 1):
    print('\t', i, end='')
for i in range(a, b + 1):
    print('\n', i, end='')
    for i2 in range(c, d + 1):
        print('\t', i * i2, end='')
