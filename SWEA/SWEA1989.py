T = int(input())

for tc in range(1, 1 + T):
    chars = input().strip()
    res = 0
    if chars == chars[::-1]:
        res = 1
    print(f'#{tc} {res}')