n = int(input())
numstack = []

for _ in range(n):
    num = int(input())
    if num == 0:
        numstack.pop()
    else :
        numstack.append(num)

print(sum(numstack))