c, r = list(map(int,input().split()))

stores = []
# c : 가로 r : 세로

roundlen = (c + r) * 2
res = 0
n = int(input())  # 상점갯수
for _ in range(n + 1):
    a, b = map(int, input().split())
    if a == 1:
        stores.append([0, b, 1])
    if a == 2:
        stores.append([r , b, -1])
    if a == 3:
        stores.append([b, 0, 2])
    if a == 4:
        stores.append([b, c, -2])


rocation = stores.pop()

for i in range(n):
    if stores[i][2] + rocation[2]:
        res += abs(stores[i][0] - rocation[0]) + abs(stores[i][1] - rocation[1])
    else: # 반대방향에 있을때
        tmp = stores[i][0] + rocation[0] + stores[i][1] + rocation[1]
        res += min(roundlen - tmp,tmp)
print(res)