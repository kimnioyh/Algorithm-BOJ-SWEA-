import sys
input = sys.stdin.readline


n = int(input())   # 노드개수
visited = [0] * (n+1) 
adjL = [[] for _ in range(n+1)]
# newadjL = [[] for _ in range(n+1)]
# parents = [[] for _ in range(n+1)]
res = 1

for _ in range(n-1):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)
    # parents[v2].append(v1)

nums = list(map(int,input().split()))
# BFS 방문순서

if nums[0] != 1:
    res = 0

i = 0
start = nums[i]
visited[start] = 1
queue = [start]
i += 1

while res and queue:
    t = queue.pop(0)

    # print(i, t, queue)

    while i != n:

        if nums[i] in adjL[t]:
            visited[nums[i]] = 1
            queue.append(nums[i])

            # print(queue)
            i += 1
        else:
            break

if i != n:
    res = 0

print(res)