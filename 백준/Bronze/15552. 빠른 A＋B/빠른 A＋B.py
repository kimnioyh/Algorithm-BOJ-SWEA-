import sys

input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    print(sum(list(map(int, input().strip().split()))))