import re
x = input()
print(len(re.findall("(c|C|g|G)", x)) / len(x) * 100)
