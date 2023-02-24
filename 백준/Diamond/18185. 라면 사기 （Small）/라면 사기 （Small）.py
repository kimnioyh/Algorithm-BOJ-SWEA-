n = int(input())
lst = list(map(int, input().split())) + [0, 0]

def ram_sam(i, k):
    lst[i] -= k
    lst[i + 1] -= k
    lst[i + 2] -= k
    return k * 7

def ram_dul(i, k):
    lst[i] -= k
    lst[i + 1] -= k
    return k * 5

def ram_hana(i):
    k = lst[i]
    lst[i] -= k
    return k * 3

res = 0

for i in range(n):

    if lst[i + 1] > lst[i + 2]:
        res += ram_dul(i, min(lst[i], lst[i + 1]-lst[i + 2]))

    sam = min(lst[i], lst[i + 1], lst[i + 2])
    if sam:
        res += ram_sam(i, sam)

    dul = min(lst[i], lst[i + 1])
    if dul:
        res += ram_dul(i, dul)

    else:
        res += ram_hana(i)
print(res)