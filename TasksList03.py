l = [int(i) for i in input().split()]
x = int(input())
k,h = 0,0
for k,h in enumerate(l):
    if x == h:
        print(k, end=' ')
if x not in list(l):
    print('Отсутствует', end=' ')
