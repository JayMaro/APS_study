from collections import deque


def bfs(s):
    q = deque(s)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    day = -1
    while q:
        x, y, day = q.popleft()
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M and arr[xx][yy] == 0 and v[xx][yy] == -1:
                q.append((xx, yy, day+1))
                v[xx][yy] = day + 1
                arr[xx][yy] = 1
    return day


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[-1]*M for _ in range(N)]
s = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            s.append((i, j, 0))
            v[i][j] = 0

res = bfs(s)
flag = True
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = False
if flag:
    print(res)
else:
    print(-1)

