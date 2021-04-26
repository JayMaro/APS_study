# 방문체크 꼭 필수!! 까먹지 말기

from collections import deque


def bfs(num):
    stack = [(num, 0)]
    stack = deque(stack)
    while stack:
        x, y = stack.popleft()
        if x == e:
            return y
        for i in range(4):
            if i == 0:
                if x + 1 > 1000000 or visited[x+1] == 1:
                    continue
                visited[x + 1] = 1
                stack.append((x + 1, y + 1))
            elif i == 1:
                if x - 1 < 0 or visited[x-1] == 1:
                    continue
                visited[x - 1] = 1
                stack.append((x - 1, y + 1))
            elif i == 2:
                if x * 2 > 1000000 or visited[x*2] == 1:
                    continue
                visited[x * 2] = 1
                stack.append((x * 2, y + 1))
            elif i == 3:
                if x - 10 < 0 or visited[x-10] == 1:
                    continue
                visited[x - 10] = 1
                stack.append((x - 10, y + 1))


T = int(input())
for tc in range(1, T + 1):
    s, e = map(int, input().split())
    visited = [0] * 1000001
    res = bfs(s)
    print('#{} {}'.format(tc, res))