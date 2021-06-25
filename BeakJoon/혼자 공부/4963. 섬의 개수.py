from collections import deque


def bfs(i, j):
    q = [(i, j)]
    dx = [1, 0, -1, 0, 1, -1, 1, -1]
    dy = [0, 1, 0, -1, 1, -1, -1, 1]
    q = deque(q)
    while q:
        x, y = q.popleft()
        for i in range(8):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and map_arr[xx][yy] == 1:
                q.append((xx, yy))
                map_arr[xx][yy] = 0


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    map_arr = [list(map(int ,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if map_arr[i][j] == 1:
                bfs(i, j)
                cnt += 1


    print(cnt)