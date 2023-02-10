l = int(input())

chars = input()

hashnum = 0

for i in range(len(chars)):
    hashnum += (ord(chars[i]) - ord('a') + 1) * (31 ** i)

print(hashnum % 1234567891)