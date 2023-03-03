arr = [[0] * 100 for _ in range(100)]

area = 0
for _ in range(int(input())):
    a, b = map(int,input().split())
    for i in range(a, min(a+10, 100)):
        for j in range(b, min(b+10, 100)):
            if arr[i][j] == 0:
                arr[i][j] = 1
                area += 1
print(area)

