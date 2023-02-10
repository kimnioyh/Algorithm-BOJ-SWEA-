a,b,k = map(int, input().split())
cnt = (k - a)//(a-b) + 1 if (k-a)//(a-b) == (k-a)/(a-b) else (k-a)//(a-b) + 2

print(cnt)