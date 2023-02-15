V = int(input())
E = int(input())

adjL = [[] for _ in range(V + 1)]
stack = []
infected = [0] * (V + 1)

for _ in range(E):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

v = 1
infected[v] = 1
cnt = 0

while True:
    for w in adjL[v]:
        if not infected[w]:
            stack.append(v)
            v = w
            infected[w] = 1
            cnt += 1
            break
    else:
        if stack :
            v = stack.pop()
        else :
            break

print(cnt)