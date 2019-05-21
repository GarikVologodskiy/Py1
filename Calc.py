a,b = float(input('Юленька, введи первое число: ')),float(input('Юленька, введи второе число: '))
i = input('Юльчик, введи операцию: ')
import operator
oper = {'+':operator.add,'-':operator.sub,'/':operator.truediv,'*':operator.mul,'mod':operator.mod,'div':operator.floordiv,'pow':operator.pow}
if b == 0 and i in ('/','div','mod'):
    print('Деление на 0!')
else:
        result = oper[i](a,b)
        print('Результат: ',result)
