def my_len(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt


def rot_90_board(board):
    boardlen = my_len(board)
    new_board = [[0] * boardlen for _ in range(boardlen)]
    for i in range(N):
        for j in range(N):
           new_board[j][boardlen - 1 - i] = board[i][j]
    return new_board


def ILtoS(lst):
    return ''.join(list(map(str, lst)))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())   # 배열의 길이를 받아옴
    board = [list(map(int, input().split())) for _ in range(N)] # N * N 배열을 입력

    res_board1 = rot_90_board(board)
    res_board2 = rot_90_board(res_board1)
    res_board3 = rot_90_board(res_board2)

    print(f'#{tc}')
    for i in range(N):
        print(ILtoS(res_board1[i])+ ' ' +ILtoS(res_board2[i])+  ' ' +ILtoS(res_board3[i]))
