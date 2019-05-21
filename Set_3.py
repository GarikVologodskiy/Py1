d = {}
n = int(input('Please input tne number: '))
for x in range(n):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])
