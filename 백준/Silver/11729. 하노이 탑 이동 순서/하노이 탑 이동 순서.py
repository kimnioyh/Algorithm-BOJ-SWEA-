def hanoi(n,lst,left, right):
    for i in lst:
        if i != left and i != right:
            mid = i
    if n == 0 :
        return 0
    hanoi(n-1,lst,left, mid)
    print(left, right)
    hanoi(n-1,lst,mid, right)


n = int(input())

hanoicnt = [0] * 21
hanoicnt[1] = 1
hanoicnt[2] = 3
for i in range(3,n+1):
    hanoicnt[i] = 2 * hanoicnt[i-1] + 1

lst = [1,2,3]
print(hanoicnt[n])
hanoi(n,lst,1,3)

