a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b or b == c or a == c:
        if a == b and b == c:
            print('Equilateral')
        else:
            print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')