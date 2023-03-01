n = int(input())  # 1m^2 당 자라는 참외개수
dongseo = []
nambook = []
cnt = [0] * 5
for _ in range(6):
    di, length = map(int, input().split())
    cnt[di] += 1
    if di == 1 or di == 2:
        dongseo.append(length)
    if di == 3 or di == 4:
        nambook.append(length)

# 브루트 포스로 접근..
# ㄱ자 모양 : 동쪽(1): 2, 서쪽(2):1 남쪽(3): 2 북쪽(4):1
# ㄴ자 모양 : 동쪽(1): 1, 서쪽(2):2 남쪽(3): 1 북쪽(4):2
if cnt == [0,2,1,2,1] or cnt == [0,1,2,1,2]:

    maxds = max(dongseo)
    maxnb = max(nambook)

    while dongseo[0] != maxds:
        dongseo.append(dongseo.pop(0))

    while nambook[0] != maxnb:
        nambook.append(nambook.pop(0))

    res = maxnb*maxds - dongseo[1]*nambook[2]
    print(res * n)

#나머지 
else:
    maxds = max(dongseo)
    maxnb = max(nambook)

    while dongseo[0] != maxds:
        dongseo.append(dongseo.pop(0))

    while nambook[0] != maxnb:
        nambook.append(nambook.pop(0))

    res = maxnb*maxds - dongseo[2]*nambook[1]
    print(res * n)
