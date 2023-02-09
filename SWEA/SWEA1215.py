def mysum(lst):
    cnt = 0
    for i in lst:
        cnt += i
    return cnt

def mylen(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt

def checkline(line, N):
    cnt = 0
    for i in range(mylen(line) - N + 1):
        if line[i : i + N] == line[i : i + N][::-1]:
            cnt += 1
    return cnt

for tc in range(1, 11):
    N = int(input())
    board = [input() for _ in range(8)]
    rows = [checkline(board[i], N) for i in range(8)]
    columns = [checkline([board[i][j] for i in range(8)], N) for j in range(8)]
    res = mysum(rows) + mysum(columns)
    print(f'#{tc} {res}')