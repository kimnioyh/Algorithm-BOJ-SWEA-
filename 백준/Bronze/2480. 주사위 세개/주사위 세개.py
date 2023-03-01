nums = sorted(list(map(int, input().split())))

if len(nums) == len(set(nums)):
    print(max(nums) * 100)
else:
    if nums[0] == nums[1]:
        if nums[1] == nums[2]:
            print(10000 + nums[0] * 1000)
        else:
            print(1000 + nums[0] * 100)
    else:
        print(1000 + nums[1] * 100)