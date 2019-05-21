line, matrix, lI = input(), [], 0

while line != 'end':
    matrix +=[[int(i) for i in line.split()]]
    line = input()
    lI += 1

lJ = len(matrix[0])

[([print(matrix[i - 1][j] + matrix[i][j - 1] + matrix[i][(j + 1) % lJ] + matrix[(i + 1) % lI][j], end=' ') for j in range(lJ)], print()) for i in range(lI)]


'''
Множественное присвоение в одну строку лучше чем отдельные

2.Оператор += лучше чем метод .append

3.Функция len() хуже чем цикл с +=

4.....
'''
