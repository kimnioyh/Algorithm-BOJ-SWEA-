import sys

n = int(input())
res = [0] * n

for i in range(n):
    res[i] = int(sys.stdin.readline().strip())

print(*sorted(res),sep='\n')