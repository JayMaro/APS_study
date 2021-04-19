from collections import deque

N = int(input())
s = deque()
command_lst = [input().split() for _ in range(N)]
for command in command_lst:
    if command[0] == 'push_back':
        s.append(command[1])
    elif command[0] == 'push_front':
        s.appendleft(command[1])
    elif command[0] == 'pop_front':
        if s:
            print(s.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(s))
    elif command[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif command[0] == 'back':
        if s:
            print(s[-1])
        else:
            print(-1)
    elif command[0] == 'front':
        if s:
            print(s[0])
        else:
            print(-1)