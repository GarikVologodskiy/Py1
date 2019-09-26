import requests
import re

with open ('C:/Distrib/Python/dataset_3378_2.txt', 'r') as inf:
    url = inf.readline().strip()

    # Проверка выдернутого url'а
    print(url)

req=requests.get(url)
with open ('C:/Distrib/Python/349.txt', 'w') as inf1:
    inf1.write(req.text)

with open ('C:/Distrib/Python/349.txt', 'r') as inf1:
    with open ('C:/Distrib/Python/350.txt', 'w') as inf2:
        res_count = len(open('C:/Distrib/Python/349.txt').readlines())
        inf2.write(str(res_count))
        # Проверка количества строк
        print(len(open('C:/Distrib/Python/349.txt').readlines()))


'''
# Возвращает количество без пустых строк
res_count = len(rerf.findall(r"[\n']+?", open('C:/Distrib/Python/349.txt').read()))
        inf2.write(str(res_count))
        # Проверка количества строк
        print(len(re.findall(r"[\n']+?", open('C:/Distrib/Python/349.txt').read())))
'''

'''
# Возвращает количество с пустыми строками
print(len(re.findall(r"[\n']+?", open('C:/Distrib/Python/349.txt').read())))
'''
