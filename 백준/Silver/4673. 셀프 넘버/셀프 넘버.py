i = 0
while i <= 10000:
    i += 1
    for j in range(1, i):
        k = j
        sums = k
        while k != 0:
            sums += k % 10
            k = k // 10
        if i == sums:
            break
    else:
        print(i)
