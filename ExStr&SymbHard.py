s=input()
j=len(s)
c=1
for i in range(j):
    if i==(j-1):
        print(s[i]+str(c),end='')
    else:
        if s[i]==s[i+1]:
            c+=1
        else:
            print(s[i]+str(c),end='')
            c=1
