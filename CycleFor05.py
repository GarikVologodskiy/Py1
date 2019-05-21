# put your python code here
a, b, c, d = (int(input()) for i in (1, 2, 3, 4))
for i in range(a, b + 1):
  if i == a:
    print(end="\t")
    for f in range(c, d + 1):
      print(f, end="\t")
  print()
  print(i, end="\t")
  for j in range(c, d + 1):
    print(i * j,end="\t")
