n, m = map(int, input().split())

board = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
board = [[0] * (m+2)] + board + [[0] * (m+2)]
visited = [[0] * (m+2) for _ in range(n+2)]
paintcnt = 0
maxarea = 0

delta = ((0,1),(0,-1),(1,0),(-1,0))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i][j] and not visited[i][j]:
            area = 1
            queue = [(i,j)]
            paintcnt += 1
            while queue:
                y,x = queue.pop(0)
                visited[i][j] = 1
                for dy, dx in delta:
                    ny = y + dy
                    nx = x + dx
                    if board[ny][nx] and not visited[ny][nx]:
                        queue.append((ny,nx))
                        visited[ny][nx] = 1
                        area += 1
            if maxarea < area:
                maxarea = area
print(paintcnt)
print(maxarea)