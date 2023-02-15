chars = input()
newchars = ''
stack = []
ops = '+-*/()'
isp = {'+':1,'-':1,'*':2,'/':2,'(':0}
icp = {'+':1,'-':1,'*':2,'/':2,'(':3}

for char in chars:
    if char not in ops:  # 문자일때
        newchars += char
    
    else :
        if char == ')':
            while stack[-1] != '(':
                newchars += stack.pop()
            stack.pop()
        elif stack:
            if isp[stack[-1]] < icp[char]:  # + 들어있고 *들어옴 a+b*c -> abc*+
                stack.append(char)
            else :                          # * 들어있고 + 들어옴 a*b+c -> ab*c+
                while isp[stack[-1]] >= icp[char]:
                    newchars += stack.pop()
                    if not stack:
                        break
                stack.append(char)
        else :
            stack.append(char)

while stack:
    newchars += stack.pop()

print(newchars)