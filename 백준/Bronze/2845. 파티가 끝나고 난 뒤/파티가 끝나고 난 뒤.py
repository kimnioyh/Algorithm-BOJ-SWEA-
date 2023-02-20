a, b = map(int, input().split())
nums = list(map(int, input().split()))

peoplenum = a * b

for num in nums:
    print(num - peoplenum, end=' ')