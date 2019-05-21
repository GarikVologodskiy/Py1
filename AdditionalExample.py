# Создаётся функция, которая и будет всё делать
def zm(n):
    # Переменной dx присваивается значение 1
    # Переменной dy присваивается значение 0
    # Обычно dx и dy - это некие приращения для переменных x и y
    dx, dy = 1, 0
    # Переменным x и y присваивается значение 0
    x, y = 0, 0
    # Создаётся список списков
    # Это матрица n*n
    # Пока все её элементы - пустые (None)
    arr = [[None] * n for _ in range(n)]
    # Выполняется перебор
    # Для переменной i последовательно перебираем значения от 1 до (n-квадрат + 1)
    for i in range(1, n**2+1):
        # Элементу матрицы с координатами x и y присваивается значение i
        # Эта строчка будет присваивать последовательные натуральные числа
        # тем ячейкам, которые перебирает код чуть ниже
        arr[x][y] = i
        # Создаются временные переменные nx и ny
        # в которых вычисляются новые значения для x и y
        # для этого к старым значенииям прибавляются приращения
        nx, ny = x+dx, y+dy
        # Если всё нормально, и индекс не выскочил за пределы матрицы
        # или не наткнулся на уже занятую ячейку
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            # то эти значения и оставляются
            x, y = nx, ny
        else:
            # а если индекс выскочил за границу матрицы
            # или наткнулся на уже занятую ячейку
            # то разворачиваемся на 90 градусов
            # путем замены приращения по x и y друг на друга
            # а минус нужен, чтобы он не ходил только вправо или вниз, 
            # а чередовал с движениями вверх или влево. 
            # Так и получается спираль 
            dx, dy = -dy, dx
            # и используем уже это изменённое движение для новых значений x и y
            x, y = x+dx, y+dy
    # После того, как перебрали все элементы, 
    # печатаем то, что получилось
    for x in list(zip(*arr)):
        print(*x)

# А здесь вся вышеописанная функция
# вызывается с аргументом, который вводит пользователь с клавиатуры
zm(int(input()))
