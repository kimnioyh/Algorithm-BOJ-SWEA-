T = int(input())

for tc in range(1, 1 + T):
    stack = []
    PS = input()

    for char in PS :
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                stack.pop()
            else :
                print('NO')
                break
    else :
        if stack :
            print('NO')
        else :
            print('YES')