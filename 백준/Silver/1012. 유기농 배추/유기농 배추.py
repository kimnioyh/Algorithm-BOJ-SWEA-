T = int(input())

for tc in range(1, 1 + T):
    M , N , K = map(int, input().split())

    field = [[0] * (M + 2) for _ in range(N + 2)] # N * M 밭 생성
    visited = [[0] * (M + 2) for _ in range(N + 2)]
    yx_move = [[1,0],[-1,0],[0,1],[0, -1]]
    stack = []
    cnt = 0

    for _ in range(K):
        b, a = map(int, input().split())
        field[a + 1][b + 1] = 1
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if field[i][j] and not visited[i][j] :
                v = (i, j)
                visited[i][j] = 1
                cnt += 1

                while True:
                    for y, x in yx_move:
                        if field[v[0] + y][v[1] + x] and not visited[v[0] + y][v[1] + x]:
                            stack.append(v)
                            v = v[0] + y , v[1] + x
                            visited[v[0]][v[1]] = 1
                            break
                    else :
                        if stack :
                            v = stack.pop()
                        else :
                            break

    print(cnt)
                            