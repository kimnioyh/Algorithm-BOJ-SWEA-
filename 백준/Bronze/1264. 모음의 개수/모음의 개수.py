while True:
    chars = input()
    cnt = 0
    vowels = 'aeiouAEIOU'

    if chars == '#':
        break

    for char in chars:
        if char in vowels:
            cnt += 1
    print(cnt)