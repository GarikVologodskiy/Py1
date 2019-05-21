def sf(n)

    tx, ty = 1, 0
    x, y = 0, 0
    matr = [[0]] * n for i in range(n)]
    for i in range(1, n**2+1):
        matr[x][y] = i
        nx, ny = x+tx, y+dy
        if 0 <= nx < n and 0 <= ny <n and not matr[nx, ny]:
            x, y = nx, ny
        else:
            tx, ty = -ty, tx
            x, y = x+tx, y+ty
    for x in list(zip(*matr)):
        print(*x)
        

