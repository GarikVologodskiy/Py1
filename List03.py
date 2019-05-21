l=[int(i) for i in input().split()]
for i in set(l):
    if l.count(i)>1:
        print(i, end=' ')
