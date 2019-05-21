'''
l=[int(i) for i in input().split()]
m=l[0]
for i in l:
    if m > i:
        m = i
print(m)
'''

n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
print(a)
        
