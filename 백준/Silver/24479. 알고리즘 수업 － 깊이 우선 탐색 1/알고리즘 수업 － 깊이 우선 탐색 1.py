import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E, R = map(int, input().split())

visited = [0] * (V + 1)
adjL = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    adjL[a] += [b]
    adjL[b] += [a]

for i in range(1, V + 1):
    adjL[i].sort()

v = R
cnt = 0


def DFS(adjL, v, visited):
    global cnt
    cnt += 1
    visited[v] = cnt
    for w in adjL[v]:
        if not visited[w]:
            DFS(adjL, w, visited)

DFS(adjL,v,visited)

print(*visited[1:], sep='\n')