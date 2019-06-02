import re
with open (r"C:\Distrib\Python\dataset_3363_2.txt", "r") as file_in:
    f1 = file_in.readline().strip()
    f1 = re.split("(\d*)", f1)[:-1]
out = open (r"C:\\Distrib\\Python\\dataset_3363_3.txt", "w")
for i in range(len(f1)):
    if f1[i].isdigit() == 0:
        output = f1[i]*int(f1[i+1])
        print(output)
        out.write(output)
    else:        
        continue
out.close()


'''
 open (r"C:\\Distrib\\Python\\dataset_3363_3.txt", "w") as f_out:
        f_out.write(f1[i]*int(f1[i]))

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
            
   '''         
    

