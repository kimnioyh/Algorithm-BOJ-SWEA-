n = int(input())

isused1 = [0] * n  #열을 확인하는 
isused2 = [0] * (2 * n - 1) # 우측 대각선확인 (x + y)
isused3 = [0] * (2 * n - 1) # x - y + n -1 이 동일한지.
cnt = 0

def nqueen(k):
    global cnt

    if k == n:
        cnt += 1
        return

    for i in range(n):  # 현재좌표 [k][i]
        if not isused1[i] and not isused2[k + i] and not isused3[i - k + n -1] :
            isused1[i] = 1
            isused2[k + i] = 1
            isused3[i - k + n -1] = 1
            nqueen(k + 1)
            isused1[i] = 0
            isused2[k + i] = 0
            isused3[i - k + n - 1] = 0


# 열과 대각선
# 같은열 -> y좌표.
# 대각선 -> y-x , y +x 가 일치하는지 확인.
nqueen(0)

print(cnt)
