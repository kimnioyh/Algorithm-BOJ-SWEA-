n = int(input())

lst = []
res = []
for i in range(1, n + 1):
    lst.append(list(map(int, input().split())) + [i])

for i in range(n): # 정렬완료된 인덱스
    cnt = 1
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    lst[i].append(cnt)

for i in range(n):
    print(lst[i][3], end = ' ')
