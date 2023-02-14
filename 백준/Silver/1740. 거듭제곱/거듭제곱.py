N = int(input())

numlst = []
res = 0

while N > 0:
    numlst.append(N % 2)
    N = N // 2
l = 0

for i in numlst :
    res += i * (3 ** l)
    l += 1

print(res)