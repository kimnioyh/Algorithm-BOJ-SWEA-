N = int(input())

res = 1

while N > 1:
    res *= N
    N -= 1
    
print(res)