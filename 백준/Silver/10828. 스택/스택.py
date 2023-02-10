import sys

pseudo_stack = []

N = int(sys.stdin.readline().strip())
for i in range(N):
    command = sys.stdin.readline().strip()
    if 'push' in command.split():
        pseudo_stack.append(int(command.split()[1]))
    elif command == 'top':
        if pseudo_stack :
            print(pseudo_stack[-1])
        else :
            print(-1)
    elif command == 'size':
        print(len(pseudo_stack))
    elif command == 'empty':
        if pseudo_stack :
            print(0)
        else :
            print(1)
    elif command == 'pop':
        if pseudo_stack:
            print(pseudo_stack.pop())
        else :
            print(-1)