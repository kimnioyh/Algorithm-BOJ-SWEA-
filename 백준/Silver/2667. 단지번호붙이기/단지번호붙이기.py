N = int(input())

delta = ((0,1),(0,-1),(1,0),(-1,0))

board = [[0] + list(map(int,input())) + [0] for _ in range(N)]
board = [[0] * (N + 2)] + board + [[0] * (N + 2)]
visited = [[0] * (N + 2) for _ in range(N + 2)]

cnt = 0


def DFS(y, x):
    global cnt
    visited[y][x] = 1
    cnt += 1
    for dy, dx in delta:
        ny = y + dy
        nx = x + dx
        if board[ny][nx] and not visited[ny][nx]:
            DFS(ny, nx)


areacnt = 0
cnt_lst = []
for i in range(1, 1 + N):
    for j in range(1, 1 + N):
        cnt = 0
        if board[i][j] and not visited[i][j]:
            DFS(i, j)
            areacnt += 1
            cnt_lst.append(cnt)
cnt_lst.sort()
print(areacnt,*cnt_lst,sep = '\n')