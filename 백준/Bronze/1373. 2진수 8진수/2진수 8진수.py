N = input()[::-1]
i = 0
res_list = []

while i < len(N):
    res = 0
    c = 1

    for num in N[i:i + 3]:
        res += int(num) * c
        c *= 2
        
    res_list.append(res)
    i += 3

print(*res_list[::-1],sep='')