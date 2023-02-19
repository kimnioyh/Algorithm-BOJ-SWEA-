chars = input()
n = len(chars)

cnt = 0
res = 0
for i in range(1 , n) :
    if chars[i] == '(':
        cnt += 1
    else:    #닫는괄호
        if chars[i - 1] == '(':
            res += cnt
        else:
            res += 1
        cnt -= 1
print(res)