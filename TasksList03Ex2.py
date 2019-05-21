lst = [int(i) for i in input().split()]
x = int(input())
cond = True
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        cond = False
if cond:
    print('Отсутствует')
