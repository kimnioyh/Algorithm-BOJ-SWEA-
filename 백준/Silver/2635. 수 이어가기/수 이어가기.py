n = int(input())

maxcnt = 2
maxlst = [n,1]
for i in range(n+1):
    s = [n, i]
    cnt = 2
    while True:
        if s[-2] - s[-1] >= 0:
            s.append(s[-2] - s[-1])
            cnt += 1
        else:
            break
    if cnt > maxcnt :
        maxcnt = cnt
        maxlst = s

print(maxcnt)
print(*maxlst)