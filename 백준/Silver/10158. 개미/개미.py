w, h = map(int, input().split())  # 가로, 세로

x, y = map(int, input().split())  # 개미 현재위치

t = int(input())  #시간


x = x + t
y = y + t


if (x // w) % 2 == 0:    # 현재 가로만큼 반전시킨횟수를 구함
    x = x % w
else :
    x = w - (x % w)


if (y // h) % 2 == 0:
    y = y % h
else :
    y = h - (y % h)

print(x, y)