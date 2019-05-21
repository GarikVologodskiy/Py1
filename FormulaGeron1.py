def geron(a,b,c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(geron(*[float(input()) for i in range(3)]))
