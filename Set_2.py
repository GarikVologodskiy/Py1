d = {'C000а1':['Иванов','Петров', 'Сидоров'], 'C001а2':['Бахсотиани','Брыльский', 'Гераменко']}
for key in d:
    print(key, end=' ')
for key in d.keys():
    print(key, end=' ')
for value in d.values():
    print(value, end=' ')
for key, value in d.items():
   print(key, value, end=';')
