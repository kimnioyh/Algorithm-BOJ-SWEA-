import sys
input = sys.stdin.readline

cnt = [[0, i] for i in range(-4000, 4001)]

n = int(input())
numlist = [0] * n

for i in range(n):
    numlist[i] = int(input())
    cnt[numlist[i] - 4001][0] += 1
cnt.sort(key = lambda x: (-x[0], x[1]))
numlist.sort()

print(round(sum(numlist)/n))
print(numlist[n//2])
if cnt[0][0] == cnt[1][0]:
    print(cnt[1][1])
else :
    print(cnt[0][1])
print(numlist[-1] - numlist[0])