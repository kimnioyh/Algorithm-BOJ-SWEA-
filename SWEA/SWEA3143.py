def my_len(lst):
    cnt = 0
    for _ in lst :
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, 1 + T):
    a, b = input().split()   # A에서 B 찾기
    res = my_len(a)
    b_len = my_len(b)
    i = 0

    while i < my_len(a):
        if a[i:i + b_len] == b:
            res -= b_len - 1
            i += b_len
        else :
            i += 1

    print(f'#{tc} {res}')