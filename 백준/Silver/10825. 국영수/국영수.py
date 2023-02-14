import sys

n = int(input())

score_list = [0] * n

for i in range(n):
    score_list[i] = sys.stdin.readline().strip().split()
    for j in range(1,4):
        score_list[i][j] = int(score_list[i][j])

score_list.sort(key = lambda x : (- x[1],x[2],-x[3],x[0]))

for k in range(n):
    print(score_list[k][0])