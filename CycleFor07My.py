a,b = (int(input()) for i in range(2))
summ = 0
c = 0
for i in range(a,b+1):
    if i % 3 == 0:
        summ+=i
        c += 1
print(summ/c)
