n, m = map(int, input().split())

numlist = list(map(int, input().split()))

sumlist = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmpsum = numlist[i] + numlist[j] + numlist[k]
            if tmpsum <= m:
                sumlist.append(tmpsum)


print(max(sumlist))