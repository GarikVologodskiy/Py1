def sf(n):

    x, y, tx, ty = 0, 0, 1, 0
    matr = [[None] * n for _ in range(n)]
    for i in range(1, n**2+1):
        matr[x][y] = i
        nx, ny = x+tx, y+ty
        if 0 <= nx < n and 0 <= ny < n and not matr[nx][ny]:
            x, y = nx, ny
        else:
            tx, ty = -ty, tx
            x, y = x+tx, y+ty
    for x in list(zip(*matr)):
        print(*x)
        
sf(int(input()))
