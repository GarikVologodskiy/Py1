b = ''

while True:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        b = b + str(a) + '\n'
print (b)


'''
b = ' '  - создаём пустую строку,  в которую будем записывать числа, удовлетворяющие условиям, чтобы потом их разом вывести на экран
b = b + str(a) + '\n' - добавляем очередное подходящее число в строку b, меняя тип на стринг, и прибавляем в конце символ переноса на следующую строку
'''