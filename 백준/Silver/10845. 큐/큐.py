import sys

pseudo_queue = []

N = int(sys.stdin.readline().strip())

for i in range(N):
    command = sys.stdin.readline().strip()
    if 'push' in command.split():
        pseudo_queue.append(int(command.split()[1]))
    elif command == 'back':
        if pseudo_queue :
            print(pseudo_queue[-1])
        else :
            print(-1)
    elif command == 'front':
        if pseudo_queue :
            print(pseudo_queue[0])
        else :
            print(-1)  
    elif command == 'size':
        print(len(pseudo_queue))
    elif command == 'empty':
        if pseudo_queue :
            print(0)
        else :
            print(1)
    elif command == 'pop':
        if pseudo_queue:
            print(pseudo_queue.pop(0))
        else :
            print(-1)