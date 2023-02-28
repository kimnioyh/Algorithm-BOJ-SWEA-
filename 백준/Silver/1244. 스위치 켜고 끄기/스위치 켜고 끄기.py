n = int(input())
switch = [0] + list(map(int, input().split()))
studs = int(input())

for i in range(studs):
    gen, num = map(int, input().split())

    if gen == 1:  # 남학생일 때
        num_ = num
        while num_ <= n:
            switch[num_] = (switch[num_] + 1) % 2
            num_ += num

    if gen == 2:  # 여학생일 때
        for k in range(1, n + 1):
            if 1<= (num - k) <= n and 1 <= num+k <=n:
                if switch[num-k] == switch[num+k]:
                    continue
                else:
                    break
            else:
                break
        k = k - 1
        for num_ in range(num-k, num+k+1):
            switch[num_] = (switch[num_] + 1) % 2

linenum = n // 20

for i in range(0, linenum + 1):
    print(*switch[i*20 + 1: (i+1)*20 +1])