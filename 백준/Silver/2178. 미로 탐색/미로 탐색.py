N, M = map(int, input().split())

mv = ((1,0),(-1,0),(0,1),(0,-1))

board = [[0] + list(map(int, input())) + [0] for _ in range(N)]
board = [[0] * (M+2)] + board + [[0] * (M+2)]
visited = [[0] * (M+2) for _ in range(N+2)]
# print(*board,sep='\n')
res = []
queue = []

y,x = (1,1)
visited[y][x] = 1
queue.append((y,x,1))
res_lst = []
while queue:
    y, x, res = queue.pop(0)
    # print(y, x, res)
    for dy, dx in mv:
        ny = y + dy
        nx = x + dx
        if ny == N and nx == M :
            res_lst.append(res + 1)
        if board[ny][nx] and not visited[ny][nx]:
            queue.append((ny,nx,res + 1))
            visited[ny][nx] = 1
print(min(res_lst))