


delta = ((1,0),(0,1),(1,1),(1,-1))


def check(lst):
    bingocnt = 0

    for i in range(5):
        for j in range(5):

            if lst[i][j]:

                for di, dj in delta:

                    for k in range(1,5):
                        ni = i + di * k
                        nj = j + dj * k

                        if not (0 <= ni < 5 and 0 <= nj < 5):
                            break

                        if not lst[ni][nj]:
                            break
                    else:
                        bingocnt += 1

    return bingocnt


arr = [list(map(int, input().split())) for _ in range(5)]

checkboard = [[0]*5 for _ in range(5)]


talchool = 0
callcnt = 0

for _ in range(5):
    calls = list(map(int,input().split()))

    for call in calls:
        callcnt += 1

        for y in range(5):
            for x in range(5):

                if arr[y][x] == call:
                    checkboard[y][x] = 1
                    # print(*checkboard, sep='\n')
                    # print(callcnt)
                if check(checkboard) >= 3:
                    # print(*checkboard, sep='\n')
                    talchool = 1
                    break

            if talchool:
                break
        if talchool:
            break
    if talchool:
        break

print(callcnt)

