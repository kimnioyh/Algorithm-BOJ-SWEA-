n, m = map(int, input().split())
arr = [0] * 10
isused = [0] * 10



# k까지 수를 택한 상황에서 arr[k]를 선택하는 함수
def backtrack(k):
    if k == m:
        for i in range(m):
            print(arr[i], end = ' ')
        print()
    else :
        for i in range(1, 1 + n): # for 문 안 쪽이 핵심임.
            if not isused[i]:
                arr[k] = i 
                isused[i] = 1
                backtrack(k + 1)
                isused[i] = 0
                
backtrack(0)