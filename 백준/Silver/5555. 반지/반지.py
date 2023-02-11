# 입력받은 문자열을 복사해 2번받음

pattern = input()
N = int(input())
cnt = 0

for _ in range(N):
    if pattern in (input() * 2):
        cnt += 1

print(cnt)