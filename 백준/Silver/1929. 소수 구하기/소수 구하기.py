n, m = map(int, input().split())
if n <= 2 :
    print(2)
    n = 2

if n % 2 == 0:
    n = n + 1


for i in range(n, m + 1, 2):
    for j in range(2, int(i**(1/2)) + 2):
        if i % j == 0:
            break
    else :
        print(i)