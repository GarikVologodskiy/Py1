i = 0
while i < 5:
    a,b =input().split()
    a = int(a)
    b = int(b)
    if a==0 and b==0:
        break # досрочно завершаем цикл
    if a==0 or b==0:
        continue # игнорируем и переходим к следующей операции
    print(a*b)
    i += 1
else:
        print('Выведено 5 пар чисел')
