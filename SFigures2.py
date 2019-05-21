s = {1: lambda r: 3.14  * r**2, 2: lambda a, b: a * b, 3: lambda a, b, c: ((a+b+c)/2*(b+c-a)/2*(a+c-b)/2*(a+b-c)/2)**0.5}
f = {'круг': 1, 'прямоугольник': 2, 'треугольник': 3}
args = [float(input()) for _ in range(f[input()])]
print(s[len(args)](*args))
