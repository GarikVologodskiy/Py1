a,b,c,d = int(input()),int(input()),int(input()),int(input())
while a<=b<=10 and c<=d<=10:
    for i in range (1,10):
        for j in (i,):
            print(a*c, a*d, b*c, b*d, '\t')
    else:
        break
    
