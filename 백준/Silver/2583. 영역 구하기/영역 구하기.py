m,n,k = map(int, input().split())

# 가로 n , 세로 m
delta = ((0,1),(0,-1),(1,0),(-1,0))
board = [[1 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    a1, a2, b1, b2 = map(int,input().split())
    # board[a2][a1] ~ board[b2][b1]
    for i in range(a2,b2):
        for j in range(a1,b1):
            board[i][j] = 0
visited = [[0 for _ in range(n)] for _ in range(m)]
areacnt = 0
arealist = []
for i in range(m):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            area = 1
            queue = [(i,j)]
            areacnt += 1
            while queue:
                y,x = queue.pop(0)
                visited[i][j] = 1
                for dy, dx in delta:
                    ny = y + dy
                    nx = x + dx
                    if 0<=ny<m and 0<=nx<n:
                        if board[ny][nx] and not visited[ny][nx]:
                            queue.append((ny,nx))
                            visited[ny][nx] = 1
                            area += 1
            arealist.append(area)
arealist.sort()
print(areacnt)
print(*arealist)