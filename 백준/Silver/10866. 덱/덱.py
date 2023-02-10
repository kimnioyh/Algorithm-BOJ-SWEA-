import sys

pseudo_deque = []

N = int(sys.stdin.readline().strip())

for i in range(N):
    command = sys.stdin.readline().strip()
    if 'push_back' in command.split():
        pseudo_deque.append(int(command.split()[1]))

    if 'push_front' in command.split():
        pseudo_deque.insert(0, int(command.split()[1]))


    elif command == 'pop_front':
        if pseudo_deque:
            print(pseudo_deque.pop(0))
        else :
            print(-1)
    elif command == 'pop_back':
        if pseudo_deque:
            print(pseudo_deque.pop())
        else :
            print(-1)    
    elif command == 'back':
        if pseudo_deque :
            print(pseudo_deque[-1])
        else :
            print(-1)
    elif command == 'front':
        if pseudo_deque :
            print(pseudo_deque[0])
        else :
            print(-1)  
    elif command == 'size':
        print(len(pseudo_deque))
    elif command == 'empty':
        if pseudo_deque :
            print(0)
        else :
            print(1)