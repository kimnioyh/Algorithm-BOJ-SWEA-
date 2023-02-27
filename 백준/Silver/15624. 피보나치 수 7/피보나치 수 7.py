
n = int(input())

a = 0 # 0, 2, 4, 6
b = 1 # 1, 3, 5, 7
if n != 0:
    while n - 1 > 0:
        a = a + b
        b = a + b
        a = a % 1000000007
        b = b % 1000000007
        n -= 2

if n == 0:
    print(a)
else:
    print(b)