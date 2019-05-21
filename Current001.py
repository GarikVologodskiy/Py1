def modify_list(l):
    lst1 = []
    for i in l:
        if i % 2 == 0:
            lst1.append(i)   
    for j in lst1:
        print(j//2, end = ', ')
        '''return(lst1)'''
x = [1, 2, 3, 4, 5]
print(modify_list(x))
    
