import sys
input = sys.stdin.readline


n = int(input())   # 노드개수
visited = [0] * (n+1) 
adjL = [[] for _ in range(n+1)]

res = 1

for _ in range(n-1):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

nums = list(map(int,input().split()))
# DFS 방문순서

if nums[0] != 1:
    res = 0



# while res and stack:
#     t = stack.pop()

#     # print(i, t, queue)
#     if nums[i] in adjL[t]:
#         visited[nums[i]] = 1
#         stack.append(nums[i])
#         i += 1
#             # print(queue)


# if i != n:
#     res = 0

# print(res)

if nums[0] != 1:
    res = 0

i = 0
start = nums[i]
visited[start] = 1
stack = [start]
i += 1
v = start

while res and stack:
    if nums[i] in adjL[v]:
        visited[nums[i]] = 1
        stack.append(v)
        v = nums[i]
        i += 1
        if i == n:
            break
    else:
        v = stack.pop()

if i != n:
    res = 0

print(res)
    # for w in adjL[v]:
    #     if not visited[w]:
    #         visited[w] = 1
    #         stack.append(v)
    #         v = w
    # else:
    #     if stack:
    #         v = stack.pop()
    #     else:
    #         break        