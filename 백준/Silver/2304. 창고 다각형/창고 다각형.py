# maxheight구간을 탐색
# maxheight구간까지
# 왼쪽에서부터 커지는 높이를 기록, 오른쪽도 마찬가지.

n = int(input())
poles = []
maxpoles = [(0,0),] # 최대높이 왼쪽좌표, 높이 기록할것.
for _ in range(n):
    left, height = map(int,input().split())
    if maxpoles[0][1] < height:
        maxpoles = [(left,height)]
    elif maxpoles[0][1] == height:
        maxpoles.append((left,height))
    poles.append((left,height))

poles.sort(key=lambda x:x[0])  #  왼쪽좌표를 기준으로 정렬
maxpoles.sort(key=lambda x:x[0])
res = (maxpoles[-1][0] - maxpoles[0][0] + 1) * maxpoles[0][1]
leftpoles = [poles[0]]
rightpoles = [poles[-1]]
while True:
    i = 0
    for j in range(1,n):
        if leftpoles[i][1] < poles[j][1]:
            leftpoles.append(poles[j])
            res += leftpoles[i][1] * (poles[j][0] - leftpoles[i][0])
            i += 1
        if poles[j][1] == maxpoles[0][1]:
            break

    i = 0
    for j in range(n-2,-1,-1):
        if rightpoles[i][1] < poles[j][1]:
            rightpoles.append(poles[j])
            res += rightpoles[i][1] * (-poles[j][0] + rightpoles[i][0])
            i += 1
        if poles[j][1] == maxpoles[0][1]:
            break
    break
print(res)


