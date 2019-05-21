spisok, search = [int(i) for i in input().split()], int(input())
if search in spisok:
    print(*[i for i, j in enumerate(spisok) if j == search])
else:
    print("Отсутствует")
