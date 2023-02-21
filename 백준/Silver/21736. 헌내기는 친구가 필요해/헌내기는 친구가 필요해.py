n, m = map(int, input().split())

res = 'TT'
delta = ((1,0), (-1,0), (0,1), (0,-1))

field = [['X'] + list(input()) + ['X'] for _ in range(n)]
field = [['X'] * (m + 2)] + field + [['X'] * (m + 2)]
# 'X'로 패딩
start = 0
cnt = 0

visited = [[0] * (m + 2) for _ in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if field[i][j] == 'I':
            start = (i, j)
            break
    if start:
        break
# 도연이 시작위치 탐색
v = start
queue = [v]

while queue:
    t = queue.pop(0)
    for y, x in delta:
        w = t[0] + y, t[1] + x
        if field[w[0]][w[1]] == 'P' and not visited[w[0]][w[1]]:
            cnt += 1
            queue.append(w)
            visited[w[0]][w[1]] = 1
        if field[w[0]][w[1]] == 'O' and not visited[w[0]][w[1]]:
            queue.append(w)
            visited[w[0]][w[1]] = 1

if cnt:
    res = cnt

print(res)
