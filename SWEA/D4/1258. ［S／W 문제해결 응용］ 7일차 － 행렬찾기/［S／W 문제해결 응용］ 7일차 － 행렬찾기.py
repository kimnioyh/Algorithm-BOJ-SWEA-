T = int(input())

delta = ((0,1),(0,-1),(1,0),(-1,0))

for tc in range(1, 1 + T):
    n = int(input())
    # n * n 행렬 (0으로 패딩할것)
    board = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    board = [[0] * (n + 2)] + board + [[0] * (n + 2)]
    visited = [[0] * (n + 2) for _ in range(n+2)]
    matrixes = []

    for i in range(1, n+1):
        for j in range(1, n+1):
            cntx = 0
            cnty = 0

            if board[i][j] and not visited[i][j]:
                for k in range(j, n + 2):
                    if not board[i][k]:
                        break
                cntx = k - j
                for l in range(i, n + 2):
                    if not board[l][j]:
                        break
                cnty = l - i
                matrixes.append((cnty, cntx))

                for y in range(i, l):
                    for x in range(j, k):
                        visited[y][x] = 1

    matrixes.sort(key=lambda x : (x[0] * x[1], x[0]))
    print(f'#{tc} {len(matrixes)} ', end='')
    for row, column in matrixes:
        print(row, column, '', end='')
    print()


