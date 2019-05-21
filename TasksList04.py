def int_b(v):
    g = []
    for i in v:
            i = int(i)
            g.append(i)
    return g


a=[]
while True:
    b=[n for n in input().split()]
    if b != ['end']:
        b = int_b(b)
        a.append(b)
    else:
        break
row = len(a)
col = len(a[0])
c = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
        for j in range(col):
            if i + 1 < row and j + 1 < col:
                c[i][j]=a[i - 1][j] + a[i + 1][j] + a[i][j-1] + a[i][j + 1]
            elif i + 1 >= row and j + 1 < col:
                c[i][j]=a[i - 1][j] + a[i][j + 1] + a[i][j - 1] + a[0][j]
            elif i + 1 < row and j + 1 >= col:
                  c[i][j]=a[i][j - 1] + a[i][0] + a[i - 1][j] + a[i + 1][j]
            else:
                  c[i][j]=a[i][j - 1] + a[i][0] + a[i - 1][j] + a[0][j]
for r in c:
        for t in r:
                print(t, end=' ')
        print()
    




'''
import random
n,m=int(input()),int(input())
a=[[random.randrange(0,10) for x in range(n)] for y in range(m)]
for i in range(m):
    print (a[i])

import numpy as np
from scipy.linalg import qr

n = 3
H = np.random.randn(n, n)
Q, R = qr(H)

print (Q.dot(Q.T))
'''


##https://server.179.ru/tasks/python/2014b1/16-lists3.html
##http://qaru.site/questions/2168609/replace-specific-values-in-a-matrix-using-python
