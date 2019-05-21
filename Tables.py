n=5
a=[[1]*n]*5
a[1][1]=4
print(a)


n=4
n1=5
a=[[1]*n for i in range(n1)]
a[1][1]=3
print(a)


n=3
n1=4
a=[[5 for j in range(n)]for i in range(n1)]
a[1][1]=4
print(a)

