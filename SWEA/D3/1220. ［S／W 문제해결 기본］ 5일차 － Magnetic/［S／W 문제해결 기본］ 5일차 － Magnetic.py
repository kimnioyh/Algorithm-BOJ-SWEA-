# 열을 확인해 빨간(N극) 1 다음에 존재하는 파란(S극) 2 자성체가 존재하는지 확인.
# 파란 자성체 이후 다른 빨간자성체가 있다면 반복.
# 빨 - 파 짝 하나마다 교착상태 1개 발생

for tc in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):    # 0열 부터 확인
        j = 0
        flag = 0   # 빨간자성체를 발견못함.
        while j < N:
            if not flag and board[j][i] == 1:
                flag = 1
            if flag and board[j][i] == 2:
                flag = 0
                cnt += 1
            else:
                j += 1
    print(f'#{tc} {cnt}')