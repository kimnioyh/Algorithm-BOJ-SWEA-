n = int(input())
n_num = list(map(int, input().split()))

m = int(input())
m_num = list(map(int, input().split()))

numset = set(n_num) & set(m_num)

for i in range(m):
    if m_num[i] in numset:
        print(1)
    else :
        print(0)