def min2(a, b, c):
    if a <= c and a <= b:
        return a
    if c <= b:
        return c
    else:
        return b
'''m = min2(14, 53, 54)'''
m = min2(min2(4, 55, 44), 45, 8)
print(m)
