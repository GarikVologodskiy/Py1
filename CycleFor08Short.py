a, b , c, d = (int(input()) for i in (1, 2, 3, 4))
print('', *range(c, d+1), sep='\t')
[ print(i, *range(i * c, i * (d + 1), i), sep='\t') for i in range(a, b + 1) ]
