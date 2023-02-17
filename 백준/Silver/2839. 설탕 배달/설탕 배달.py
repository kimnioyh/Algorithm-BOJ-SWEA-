sugar = [0] * 13
sugar[2] = -1
sugar[3] = 1
sugar[4] = -1
sugar[5] = 1
sugar[6] = 2 # N%5 == 1   6이상일때
sugar[7] = -1
sugar[8] = 2 # N%5 == 3
sugar[9] = 3 # N%5 == 4   9 이상일때
sugar[10] = 2
sugar[11] = 3
sugar[12] = 4 # N%5 == 2   17 이상일때

n = int(input())
if n >= 12:
    if n % 5 == 0:
        print(n // 5)
    elif n % 5 == 1:
        print((n - 6)//5 + 2)
    elif n % 5 == 2:
        print((n - 12)//5 + 4)
    elif n % 5 == 3:
        print((n - 3)//5 + 1)
    else :
        print((n - 9)//5 + 3)
else:
    print(sugar[n])