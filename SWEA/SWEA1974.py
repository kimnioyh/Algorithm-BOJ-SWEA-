numset = set("123456789")

def checkline(lst, i):
    check = []
    for j in range(9):
        check.append(lst[j][i])
    if set(check) != numset or set(lst[i]) != numset :
        return 0
    return 1


def checksquare(lst):
    for i in range(0,9,3):
        for j in range(0,9,3):

            check = []
            for k in range(3):
                for l in range(3):
                    check.append(lst[i + k][j + l])
            if set(check) != numset:
                return 0
    return 1


T = int(input())
for tc in range(1, 1 + T):
    board = [input().split() for _ in range(9)]
    res = 1
    for i in range(9):
        if not checkline(board, i) :
            res = 0
            break
    if res :
        res = checksquare(board)

    print(f'#{tc} {res}')