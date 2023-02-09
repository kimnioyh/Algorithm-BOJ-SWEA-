T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    floor = [[ i for i in range(1, 1 + n)], ]   # 0층 초기화

    for i in range(k):      # k층 까지 반복
        floor_n = []
        sums = 0
        for j in range(n):
            sums += floor[i][j]
            floor_n.append(sums)
        floor.append(floor_n) 
    
    print(floor[k][n - 1])