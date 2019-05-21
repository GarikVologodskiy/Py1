summ=0
mult=0
while True:
    n=int(input())
    summ+=n
    mult+=n**2
    if summ==0:
        break
print(mult)
