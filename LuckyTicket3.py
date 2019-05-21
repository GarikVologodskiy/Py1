code=int(input())
a=code//100000
b=code//10000%10
c=code//1000%10
d=code//100%10
e=code//10%10
f=code%10
if a+b+c==d+e+f:
  print('Счастливый')
else:
  print('Обычный')
