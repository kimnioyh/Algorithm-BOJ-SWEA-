# n = 1: 1
# n = 2: 3
# n = 3: 5
# f(n) = f(n-1) + 2 * f(n - 2)


tile = [1] * 251
tile[1] = 1
tile[2] = 3
tile[3] = 5
for i in range(4, 251):
    tile[i] = tile[i - 1] + 2 * tile[i - 2]
    
while True:
    try:
        n = int(input())
        print(tile[n])
    except:
        break