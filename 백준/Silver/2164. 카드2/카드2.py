from collections import deque
n = int(input())

numdeque = deque([i for i in range(1, n + 1)])

while len(numdeque) > 1 :
    numdeque.popleft()
    numdeque.append(numdeque.popleft())

print(numdeque[0])