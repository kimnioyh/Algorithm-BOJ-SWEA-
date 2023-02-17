cnt = 0
n = int(input())
i = 666

while cnt < n:
    tmp = 0
    j = i
    while j != 0:
        if j % 10 == 6:
            tmp += 1
            if tmp >= 3:
                cnt +=1
                break
        else :
            tmp = 0
        j = j // 10

    i += 1

print(i - 1)