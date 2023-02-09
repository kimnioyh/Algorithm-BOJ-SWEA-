# T = int(input())

# for tc in range(1, 1 + T):
#     str1 = input()
#     str2 = input()
#     cnt = 0
#     for char in str1 :
#         if cnt < str2.count(char):
#             cnt = str2.count(char)

#     print(f'#{tc} {cnt}')

T = int(input())

for tc in range(1, 1 + T):
    str1 = input()
    str2 = input()
    set_char = set(str2) & set(str1)  # 확인할 문자 세트

    maxcnt = 0
    for char in set_char :
        cnt = 0

        for i in str2:
            if i == char :
                cnt += 1

        if maxcnt < cnt:
            maxcnt = cnt

    print(f'#{tc} {maxcnt}')