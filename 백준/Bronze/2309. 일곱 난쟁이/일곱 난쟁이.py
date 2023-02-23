
lst = []

for _ in range(9):
    lst.append(int(input()))

lst.sort()

d = sum(lst) -100

for i in range(9):
    for j in range(i + 1, 9):
        if lst[i] + lst[j] == d:
            lst.pop(j)
            lst.pop(i)
            break
    if len(lst) == 7:
        break

print(*lst, sep='\n')