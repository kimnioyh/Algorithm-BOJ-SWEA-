import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adjL = [[] for _ in range(N + 1)]


for _ in range(M):
    v1, v2 = map(int,input().split())
    adjL[v2].append(v1)

reslist = []
stack = []
maxcnt = 0
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    if not visited[i]:
        cnt = 1
        v = i
        visited[v] = 1
        while True:
            for w in adjL[v]:
                if not visited[w]:
                    stack.append(v)
                    v = w
                    visited[w] = 1
                    cnt +=1
                    break
            else:
                if stack:
                    v = stack.pop()
                else:
                    break
    reslist.append([i,cnt])
    if maxcnt < cnt:
        maxcnt = cnt
        
reslist.sort(key=lambda x : (-x[1],x[0]))

for i in range(N):
    if reslist[i][1] == maxcnt:
        print(reslist[i][0], end=' ')