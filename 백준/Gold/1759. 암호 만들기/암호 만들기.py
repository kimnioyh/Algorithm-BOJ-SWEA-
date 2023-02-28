vowels = 'aeiou'


def checkvowels(s):
    cnt = 0
    for i in s:
        if i in vowels:
            cnt += 1
    return cnt


l, c = map(int, input().split())

chars = sorted(input().split())
isused = [0] * c
arr = [0] * l


def backtrack(k, idx):  # k번째 인덱스추가하기
    if idx == c:
        for i in range(l-1,-1,-1):
            if arr[i] == 0:
                return 0

    if k == l:
        if 1 <= checkvowels(arr) < l - 1:
            print(*arr, sep='')
    else:
        for i in range(idx, c):
            if not isused[i]:
                isused[i] = 1
                arr[k] = chars[i]
                backtrack(k + 1, i)
                isused[i] = 0
                arr[k] = 0

backtrack(0,0)