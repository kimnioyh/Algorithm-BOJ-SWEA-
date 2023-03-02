n = (int(input()) // 100) * 100
s = int(input())

for i in range(0,100):
    if ( n + i ) % s == 0:
        res = str(i)
        res = (2 - len(res)) * '0' + res
        print(res)
        break