s = set()
animals = {'dog', 'cat', 'cat', 'lion', 'malibu', 'wolf'}
print(animals)
print ('lion' in animals)
print ('monkey' in animals)
if 'wodlf' not in animals:
    animals.add('gaga')
else:
    animals.clear()
print(animals)
print(len(animals))
for i in animals:
    print(*i, end = '\n')
