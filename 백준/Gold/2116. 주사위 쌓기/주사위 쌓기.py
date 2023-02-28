def find_max(lst, idx):
    # 주사위에서 한 자리를 선택 -> 나머지 숫자 중 최댓값을 구해줌
    s = 0
    for i in range(6):
        if i != idx and i != abs(idx-5):
            if lst[i] > s:
                s = lst[i]
    return s


n = int(input())  # 주사위 갯수
dices = []
for i in range(n):
    dices.append(list(map(int,input().split())))
    dices[i][3],dices[i][4] = dices[i][4],dices[i][3]
    # i 번째 숫자를 선택 -> i , abs(i - 5) 를 제외한 나머지에서 max를 구함
    # abs(i - 5)의 숫자를 찾은 후 그 인덱스에서 동일 작업.

res_max = 0
for i in range(6):
    j = 0  # 다이스 순서 0 ~ n-1
    res = 0
    res += find_max(dices[j], i)
    l = i
    while True:
        for k in range(6):
            if dices[j+1][k] == dices[j][abs(l-5)]:
                l = k
                break
        res += find_max(dices[j+1], l)
        j += 1
        if j + 1 == n:
            break
    if res_max < res:
        res_max = res

print(res_max)
