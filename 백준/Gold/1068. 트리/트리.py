def preoreder(node):
    global cnt
    if node != -1:

        for c in child[node]:
            if c != -1:
                break
        else:
            cnt +=1

        # if child1[node] == -1 and child2[node] == -1:
        #     cnt += 1

        for c in child[node]:
            if c != -1:
                preoreder(c)

        # if child1[node] != -1:    
        #     preoreder(child1[node])
        # if child2[node] != -1:
        #     preoreder(child2[node])




n = int(input())

cnt = 0
child = [[] for _ in range(n)]

parent = list(map(int, input().split()))

root = 0

for i in range(n):

    if parent[i] == -1:
        root = i
        continue

    else:
        child[ parent[i] ].append(i) 

# print(child)

delnode = int(input())

for t in range(len(child[parent[delnode]])):
    if child[parent[delnode]][t] == delnode:
        child[parent[delnode]][t] = -1

# child1[delnode] = -1
# child2[delnode] = -1
# if child1[parent[delnode]] == delnode:
#     child1[parent[delnode]] = -1
# if child2[parent[delnode]] == delnode:
#     child2[parent[delnode]] = -1
# print(child)
# print(child1)
# print(child2)
# print(parent)

preoreder(root)

if delnode == root:
    cnt = 0

print(cnt)