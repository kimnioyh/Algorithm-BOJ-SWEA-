i = int(input())
c = input()
num = int(c)
nums = list(map(int,c))
for numss in nums[::-1]:
    print(i*numss)
print(num*i)