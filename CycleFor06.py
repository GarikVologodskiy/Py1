a = int(input())
b = int(input()) + 1
c = int(input())
d = int(input()) + 1
output = ''
bag = ''
flag = True
for i1 in range(a,b): #7 - 10
 output += str(i1)
 for i in range(c,d): # 5 -6
   output += '\t' + str(i1*i)
   if flag == True:
    bag += '\t' + str(i)
 flag = False
 output += '\n'
print(bag + '\n' + output)
