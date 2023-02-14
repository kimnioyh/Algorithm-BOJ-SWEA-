import sys

N = int(sys.stdin.readline().strip())
numlist = [0] * N

for i in range(N):
    numlist[i] = int(sys.stdin.readline().strip())

key = numlist[-1]
cntstack = [key]

for j in range(N - 2, -1, -1):
    if numlist[j] > key:
        cntstack.append(numlist[j])
        key = numlist[j]

print(len(cntstack))