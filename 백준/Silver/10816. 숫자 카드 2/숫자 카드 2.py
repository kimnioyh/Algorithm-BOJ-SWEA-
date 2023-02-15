n = int(input())  #상근이가 가지고있는 숫자카드
sang_nums = list(map(int, input().split()))

m = int(input())
key_nums_ori = list(map(int, input().split()))   
# 같은 숫자가 여러 번 나올수도 있음 -> 어떻게...?

# key 숫자카드들을 상근이가 몇개나 가지고있나를 확인.
# key nums 카드를 sort.
# 상근이 카드에서 key num을 하나하나 이진탐색
key_num_count = {key : 0 for key in key_nums_ori}

key_nums = sorted(key_nums_ori)

for sang in sang_nums:
    start = 0
    end = m - 1

    while start <= end:
        middle = (end + start) // 2
        if sang > key_nums[middle]:
            start = middle + 1
        elif sang < key_nums[middle]:
            end = middle - 1
        else :
            key_num_count[sang] += 1
            break

for i in range(m):
    print(key_num_count[key_nums_ori[i]], end=' ')