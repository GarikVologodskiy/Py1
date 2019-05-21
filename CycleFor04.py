#===INIT===
x_lim_min = int(input ())
x_lim_max = int(input ())
y_lim_min = int(input ())
y_lim_max = int(input ())
#===VARS===
echo = '';
y = 0
x = 0
s = False
#===PROG===
for x in range (x_lim_max + 1):
    if(x == 0):
        for y in range(y_lim_max + 1): #for имеет собственный контроллер?..
            if(y >= y_lim_min):
                echo = echo + '\t'+ str(y)
        s = True
        y = 0

    if(x >= x_lim_min):
        echo = echo + str(x)
        for y in range(y_lim_max + 1):
            if(y >= y_lim_min):
                echo = echo + '\t'+ str(y * x)
        y = 0
        s = True

    if(s == True):
        echo = echo + '\n'

    s = False
#===ECHO===    
print (echo)
