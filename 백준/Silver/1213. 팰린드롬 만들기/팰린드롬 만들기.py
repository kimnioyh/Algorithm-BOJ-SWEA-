# 단어수를 체크 -> ABCDE .... -> 홀수개인 것이 딱 1개or 0개만 존재해야함.
# 홀수개인것을 제외. 나머지 ABCD .. 순으로 출력 (사전순으로 앞서는 것을 출력하기위해)


alp_dict = {chr(ord('A') + i) : 0 for i in range(26)} # A~ Z까지를 key로 가지는 딕셔너리 생성

chars = input()
middle = ''
res_str = ''

for char in chars:
    alp_dict[char] += 1

for alp in alp_dict:
    middle += alp * (alp_dict[alp] % 2)
    res_str += alp * (alp_dict[alp] // 2)

if len(middle) > 1:
    print("I'm Sorry Hansoo")
else :
    print(res_str+middle+res_str[::-1])