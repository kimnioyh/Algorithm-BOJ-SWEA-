while True:
    chars = input()
    stack = []
    if chars == '.':
        break
    res = 'no'
    for char in chars:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                break
    else:
        if not stack:
            res = 'yes'
    print(res)