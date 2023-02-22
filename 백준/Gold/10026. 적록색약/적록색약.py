n = int(input())

board = [[''] + list(input()) + [''] for _ in range(n)]
board = [[''] * (n + 2)] + board + [[''] * (n + 2)]

move = ((0,1),(1,0),(-1,0),(0,-1))

colors = ['R', 'B', 'G']
visited = [[0] * (n+2) for _ in range(n+2)]
visited_2 = [[0] * (n+2) for _ in range(n+2)]

cnt_norm = 0
for i in range(1, 1 + n):
    for j in range(1, 1 + n):
        if board[i][j] and not visited[i][j]:
            v = (i, j)
            queue = [v]
            visited[i][j] = 1
            cnt_norm += 1
            while queue:
                y, x = queue.pop(0)
                for dy, dx in move:
                    wy = y + dy
                    wx = x + dx
                    if board[wy][wx] and not visited[wy][wx] and board[y][x] == board[wy][wx]:
                        queue.append((wy, wx))
                        visited[wy][wx] = 1
cnt_sack = 0
for i in range(1, 1 + n):
    for j in range(1, 1 + n):
        if board[i][j] and not visited_2[i][j]:
            v = (i, j)
            queue = [v]
            visited_2[i][j] = 1
            cnt_sack += 1
            while queue:
                y, x = queue.pop(0)
                for dy, dx in move:
                    wy = y + dy
                    wx = x + dx
                    if board[y][x] == 'B':
                        if board[wy][wx] and not visited_2[wy][wx] and board[y][x] == board[wy][wx]:
                            queue.append((wy, wx))
                            visited_2[wy][wx] = 1
                    else:
                        if not visited_2[wy][wx] and board[wy][wx] != 'B' and board[wy][wx]:
                            queue.append((wy, wx))
                            visited_2[wy][wx] = 1

print(cnt_norm, cnt_sack)