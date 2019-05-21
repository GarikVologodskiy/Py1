l=[int(i) for i in input().split()]
l1 = []
if len(l) == 1:
    print(*l)                 ## Использование оператора раскрытия * для вывода списка без запятых и скобок
else:
    for i in range (len(l)-1):
        l1.append(l[i - 1] + l[i + 1])
    else:
        l1.append(l[i] + l[0])
for i in l1:                  ## Цикл для вывода содержимого нового списка
    print(i,end=' ')          ## Вывод содержимого нового списка числами с пробелами без запятых



'''
l=[int(i) for i in input().split()]
l1 = []
if len(l) == 1:
    print(l)
else:
    for i in range (len(l)-1):
        l1.append(l[i - 1] + l[i + 1])
    else:
        l1.append(l[i] + l[0])

print(*l1)
'''    
