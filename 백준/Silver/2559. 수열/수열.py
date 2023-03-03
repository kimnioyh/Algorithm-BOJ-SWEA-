n, k = map(int,input().split())  # n개의 숫자 중, k개의 연속적인 숫자
nums = list(map(int,input().split()))
hap = 0
for i in range(0,k):
    hap += nums[i]
maxhap = hap
for i in range(0, n-k):
    hap = hap - nums[i] + nums[i+k]
    if maxhap < hap:
        maxhap = hap
print(maxhap)
