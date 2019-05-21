# Read
'''
import os
os.path.join('C:', 'Distrib', 'Python', 'files','logStatic.txt')
#The First variant
a = open("C:\\Distrib\\Python\\files\\logStatic.txt", "r", encoding = "utf8") # open('logStatic.txt')
a1 = a.readline().strip()
a2 = a.read().strip()
print(a1, a2)
a.close()
'''

'''
# Write
a = open('C:\\Distrib\\Python\\files\\logStatic.txt', 'w') # open('logStatic.txt')
a.write('The Newwwewewewew\n')
a.write(str(25) + '\n')
a.write(str(555))
print(a)
a.close()
'''

'''
#The Second variant Read/Write with self-closing
with open ("C:\\Distrib\\Python\\files\\logStatic.txt", "r") as a:
    for line in a:
        line = a.read().strip()
    print(line)
'''

'''
import pathlib
path = pathlib.Path('C:/') / 'Distrib' / 'Python' / 'files'
a = pathlib.Path("logStatic.txt", "r") # open('logStatic.txt')
'''

'''
        def f(z):
    x = int(input())
    b = {}
    for i in range(x):
        z = int(input())
        if z in b.keys():
            print(b[z])
        else:
            b[z] = f[z]
            print(b[z])
'''
