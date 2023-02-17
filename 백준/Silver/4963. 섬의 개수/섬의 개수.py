while True:
    W, h = map(int, input().split())
    if W == 0 and h == 0:
        break

    board = [[0] + list(map(int, input().split())) + [0] for _ in range(h)]
    board = [[0] * (W + 2)] + board + [[0] * (W + 2)]
    # 0 패딩 하고 보드를 받아옴
    visited = [[0] * (W + 2) for _ in range(h + 2)]
    # h + 2 * w + 2 visited 배열 생성
    stack = []

    dy = [1, 1, -1, -1, 1, -1, 0, 0]
    dx = [1, -1, 1, -1, 0, 0, 1, -1]
    # 델타배열
    res = 0
    for y in range(1, 1 + h):
        for x in range(1, 1 + W):

            if board[y][x] and not visited[y][x]:
                v = (y, x)
                visited[v[0]][v[1]] = 1
                res += 1
                while True:
                    for k in range(8):
                        w = (v[0] + dy[k], v[1]+dx[k])
                        if board[w[0]][w[1]] and not visited[w[0]][w[1]]:  # 길이있고 방문안함
                            visited[w[0]][w[1]] = 1
                            stack.append(v)
                            v = w
                            break
                    else:
                        if stack:
                            v = stack.pop()
                        else:
                            break
    print(res)