import sys
print(len(sys.argv))

'''
students = []
av_m = list() #Вспомогательный список
with open (r"C:\Distrib\Python\dataset_3363_5.txt", "r") as file_in:
    with open (r"C:\Distrib\Python\dataset_3363_7.txt", "w") as file_out:
        for line in map (str.strip, file_in):
            line = list(map(int, line.split(";")[1:]))
            average_marks = sum(line) / len(line)
            file_out.write(str(average_marks) + "\n")
            students.append(line)
            length = len(students)
            print(average_marks)    
        for val in (sum(i) / length for i in zip (*students)):
                file_out.write(str(val) +  " ")       
                print(val, end = " ")
print()
         
#Счетчик строк
with open (r"C:\Distrib\Python\dataset_3363_7.txt", "r") as file_out:
    print("\n")
    l = (len(file_out.readlines()))
    print(f"Количество строк = {l}")
''' 

'''
    count = 0
    for line in file_out:
        count += 1
        print("\n")
        print(f"Количество строк = {count}")
   '''     
'''
    file_out.write(str(val)+ '\n')'''
           

'''
    for i in students:
        print('{}: {:.2f}'.format(i[2], i[-1]))
   
        parts = line.split(';')
        name = parts[0]

        rate = list(map(int, parts[1:]))
        res = sum(rate) / len(rate)

        students.append(
        (name, rate, res)
    )
with open (r"C:\Distrib\Python\dataset_3363_6.txt" "w") as file_out:
    file_out.write(students)

    
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
    

