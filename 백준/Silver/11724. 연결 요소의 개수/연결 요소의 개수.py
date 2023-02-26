import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(graph, v):
    visited[v] = 1
    for w in graph[v]:
        if not visited[w]:
            visited[w] = 1
            DFS(graph, w)

N, M = map(int,input().split())
adjL = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
cnt = 0

for _ in range(M):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

for i in range(1, N + 1):
    if not visited[i]:
        DFS(adjL, i)
        cnt += 1

print(cnt)