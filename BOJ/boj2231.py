N = int(input())
numlist = []
gen = 0

for j in range(N):
    i = j
    gen = i
    while i > 0:
        gen += i % 10
        i = i // 10
    if N == gen:
        numlist.append(j)
if numlist :
    print(min(numlist))
else :
    print(0)