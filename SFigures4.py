figura = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5], 
          'прямоугольник': [2, lambda a, b: a*b], 
          'круг': [1, lambda r: 3.14*r**2]}
f = input()
print(figura[f][1](*(float(input()) for _ in range(figura[f][0]))))
