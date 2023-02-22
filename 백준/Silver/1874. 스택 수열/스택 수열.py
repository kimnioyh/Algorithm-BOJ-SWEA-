import sys
input = sys.stdin.readline


n = int(input())

nums = [i for i in range(n, 0, -1)]
stack = []
res_list = []
res = 0

i = 0 # 스택에 들어간 숫자
for _ in range(n):
    s = int(input())
    if i < s:  # i < s (push)
        j = i
        while j < s:
            stack.append(nums.pop())
            res_list.append('+')
            i += 1
            j += 1
        if s == stack[-1]:
            stack.pop()
            res_list.append('-')
        else:
            res = 'NO'
            break
    elif i >= s: # i > s (pop) , i==s (pop)
        if stack[-1] != s:
            res = 'NO'
            break
        else:
            stack.pop()
            res_list.append('-')

if res:
    print(res)
else:
    print(*res_list, sep='\n')