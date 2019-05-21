def modify_list(l):
    count = 0
    while count != len(l):
        if l[count] % 2 != 0:
            l.pop(count)
        else:
            l[count] //= 2
            count += 1
    return l

'''print(modify_list([1, 2, 3, 4, 5, 6]))'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 10, 99, 140, 200]
print(modify_list(x))

    
