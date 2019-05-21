f = input()
if f == 'треугольник':
    a,b,c = float(input()),float(input()),float(input()) 
    p = (a + b + c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif f == 'прямоугольник':
    a,b = float(input()),float(input()) 
    print(a * b)
elif f == 'круг':
    r = float(input()) 
    print (3.14 * r**2)
else:
    print('Введен неверный тип фигуры')
