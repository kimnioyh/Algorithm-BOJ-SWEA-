# N을 입력받음
# N * N 보드를 생성 + (X로 패딩)
# 전치 보드를 생성
# '..' 이 있으면 누울수 있음. -> in 연산자 사용하기 .. 
# 오답.. 방 중간에 기둥으로 나눠질경우 ..X.. < 2개로 카운트해야됨


# 다시풀기
# N * N보드를 생성 
# 전치보드를 생성
# X로 split 후 그 리스트 안에서 '..'를 찾기 


N = int(input())
board =[input() for _ in range(N)]
col_board = []
tmpstr = ''

res = [0 , 0]   # 가로, 세로 결과값
for i in range(N):
    tmpstr = ''
    for j in range(N):
        tmpstr += board[j][i]
    col_board.append(tmpstr)

for i in range(N):
    for space in board[i].split('X'):
        if '..' in space:
            res[0] += 1

    for space in col_board[i].split('X'):
        if '..' in space:
            res[1] += 1        

print(*res)
