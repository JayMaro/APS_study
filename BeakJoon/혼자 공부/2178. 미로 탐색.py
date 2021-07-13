from collections import deque


def bfs():
    q = deque()
    q.append((1, 0, 0))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q:
        dist, x, y = q.popleft()
        if x == N-1 and y == M-1:
            return dist
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and arr[xx][yy] == 1:
                arr[xx][yy] = 0
                q.append((dist+1, xx, yy))


N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
print(bfs())
