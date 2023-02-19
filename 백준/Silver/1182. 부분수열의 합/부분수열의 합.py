N, S = map(int, input().split())

nums = list(map(int, input().split()))

cnt = 0

def powerset(k, tot):
    global cnt

    if k == N:
        if tot == S:
            cnt += 1
        return
    
    else:
        powerset(k + 1, tot + nums[k])
        powerset(k + 1, tot)

powerset(0,0)

if S == 0:
    cnt -= 1

print(cnt)