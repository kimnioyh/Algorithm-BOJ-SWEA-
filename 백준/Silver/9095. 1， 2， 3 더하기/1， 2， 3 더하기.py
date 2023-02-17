hap = [1] * 11
hap[1] = 1
hap[2] = 2
hap[3] = 4
for n in range(4, 11):
    hap[n] = hap[n-1] + hap[n-2] + hap[n-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(hap[N])