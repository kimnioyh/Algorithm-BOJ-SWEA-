N, M, V = map(int, input().split())
# 정점 개수 N, 간선수 M, 시작점 V

adjL = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

for adj in adjL:
    adj.sort()


def bfs(graph, v):
    visited = [0] * (N + 1)
    queue = []
    res = [v]

    cnt = 1
    visited[v] = cnt
    queue.append(v)
    while queue:
        t = queue.pop(0)
        for w in graph[t]:
            if not visited[w]:
                cnt += 1
                visited[w] = cnt
                queue.append(w)
                res.append(w)
    return res


def dfs(graph, v):
    visited = [0] * (N + 1)
    stack = [v]
    res = [v]
    cnt = 1
    visited[v] = cnt
    while stack:
        for w in graph[v]:
            if not visited[w]:
                stack.append(v)
                v = w
                cnt += 1
                visited[w] = cnt
                res.append(w)
                break
        else:
            v = stack.pop()
    return res


print(*dfs(adjL, V))
print(*bfs(adjL, V))