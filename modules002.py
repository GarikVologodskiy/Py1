#Solution 1
import sys
print(' '.join(sys.argv[1:]))

#Solution 2
import sys
length = len(sys.argv)
for i in range(1, length):
     print(sys.argv[i])
