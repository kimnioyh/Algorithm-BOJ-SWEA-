N = int(input())

parrents = [0] * (N + 1)
stack = []

adjL = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

v = 1
parrents[v] = 1  #대충 1번 부모 1이라고 초기화

while True :
    for w in adjL[v]:
        if not parrents[w]:
            stack.append(v)
            parrents[w] = v
            v = w
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break

print(*parrents[2:],sep='\n')