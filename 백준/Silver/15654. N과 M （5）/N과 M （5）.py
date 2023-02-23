n, m = map(int, input().split())
lst = sorted(list(map(int,input().split())))
arr = [0] * 10     # 0인덱스를 제외하고 1 ~ 9를 채울예정
isused = [0] * 10   # 0인덱스를 제외하고 1 ~ 9를 사용했는지 여부 채울 것


def backtrack(k): # k번째까지 자리를 채우고 k+1번째 자리를 채우기위해 호출.
    flag = 1
    if k == m:
        # for i in range(0, k - 1):
        #     if arr[i] <= arr[i + 1]:
        #         flag = 0
        # if flag:
        print(*arr[:k])
            # for i in range(k):
            #     print(arr[i], end=' ')
            # print()
    else:
        for i in range(len(lst)):
            if not isused[i]:
                arr[k] = lst[i]
                isused[i] = 1
                backtrack(k + 1)
                isused[i] = 0

backtrack(0)







#
# # k까지 수를 택한 상황에서 arr[k]를 선택하는 함수
# def backtrack(k):
#     if k == m:
#         for i in range(2, m + 1):
#              if arr[i] > arr[i - 1]:
#                 break
#         else:
#             for i in range(m):
#                 print(arr[i], end=' ')
#             print()
#     else:
#         for i in range(1, 1 + n):  # for 문 안 쪽이 핵심임.
#             # if not isused[i]:
#             arr[k] = i
#             # isused[i] = 1
#             backtrack(k + 1)
#                 # isused[i] = 0
#                 # backtrack(k)
#
# backtrack(0)