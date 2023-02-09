N, M = map(int,input().split())
board = [input() for _ in range(N)]
mincnt = 64
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt1 = 0
        cnt2 = 0
        for y in range(i, 8 + i):
            for x in range(j, 8 + j):
                if (x + y - i - j) % 2 == 1 :
                    if board[y][x] == 'B':
                        cnt1 += 1
                    if board[y][x] == 'W':
                        cnt2 += 1
                elif (x + y -i - j) % 2 == 0 :
                    if board[y][x] == 'W':
                        cnt1 += 1
                    if board[y][x] == 'B':
                        cnt2 += 1
        if mincnt > cnt1 :
            mincnt = cnt1
        if mincnt > cnt2 :
            mincnt = cnt2

print(mincnt)