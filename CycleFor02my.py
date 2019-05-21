a,b = int(input()),int(input())
c,d = int(input()),int(input())
print(end='\t')
for i in range (c,d+1):
    print(i,end='\t')
print()
for j in range (a,b+1):
    print(j, end='\t')
    for i in range (c,d+1):
        print(j*i,end='\t')   
    print()
