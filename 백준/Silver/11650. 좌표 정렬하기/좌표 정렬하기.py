import sys

N = int(input())
res = [ [] for _ in range(N)]

for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    res[i] = [a, b]

res.sort(key=lambda x : (x[0],x[1]))

for i in range(N):
    print(*res[i])