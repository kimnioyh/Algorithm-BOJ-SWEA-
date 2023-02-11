# N명 중 k명이 상받음. 커트라인 구해라.(상받는 사람중 가장 낮은 점수)
# 1 - N k
# N개의 데이터 입력 버블정렬로 정렬해보기.

N, k = map(int, input().split())
scores = list(map(int, input().split()))


for i in range(N - 1, 0 ,-1):
    for j in range(i):
        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

print(scores[-k])