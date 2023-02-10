T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    a = N // H + 1 * (N % H != 0)  # 호수
    b = N % H + H * (N % H == 0) # 층수

    if a >= 10:
        print(str(b) + str(a))
    else :
        print(str(b) + '0' + str(a))