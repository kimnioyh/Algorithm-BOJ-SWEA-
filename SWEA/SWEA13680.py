# 0 padding.
# 가로열 세로열에 대해 전부 cnt를 셈 ( 브루트포스로 )
# cnt를 return

T = int(input())

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    board = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]
    res_cnt = 0

    for i in range(1, N + 2):
        cnt_row = 0
        cnt_column = 0

        for j in range(1, N + 2):

            if board[i][j] :
                cnt_row += 1
            else :
                if cnt_row == K:
                    res_cnt += 1
                cnt_row = 0
            
            if board[j][i] :
                cnt_column += 1
            else :
                if cnt_column == K:
                    res_cnt += 1
                cnt_column = 0

    for i in range(N + 2):
        print(board[i])
    print(f'#{tc} {res_cnt}')