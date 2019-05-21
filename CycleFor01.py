"""
for i in 2,5,12:
    print(i*i)
"""

n = int(input())
for i in range (n):
    for j in range(n):
        print('*', end='\t')
    print()
