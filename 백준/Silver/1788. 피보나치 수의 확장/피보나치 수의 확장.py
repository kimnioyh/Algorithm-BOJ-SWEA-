
n = int(input())
res1 = 1
plusminus = 1

if n == 0:
    res1 = 0
    plusminus = 0
elif n < 0:
    res1 = -1
    if abs(n) % 2 :
        n = abs(n)
    else:
        n = abs(n)
        plusminus = -1
a = 0 # 0, 2, 4, 6
b = 1 # 1, 3, 5, 7
if n != 0:
    while n - 1 > 0:
        a = a + b
        b = a + b
        a = a % 1000000000
        b = b % 1000000000
        n -= 2

print(plusminus)
if n == 0:
    print(a)
else:
    print(b)