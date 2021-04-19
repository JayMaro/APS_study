from collections import deque

T= int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[-1]+list(input())+[-1] for _ in range(N)]
    arr = [[-1]*(M+2)] + arr + [[-1]*(M+2)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    water = deque()
    sum_move = 0
    visited = [[-2] + [-1]*M + [-2] for _ in range(N)]
    visited = [[-2] * (M + 2)] + visited + [[-2] * (M + 2)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 'W':
                water.append((i, j))
                visited[i][j] = 0

    while water:
        x, y = water.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if visited[nx][ny] == -1:
                water.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                sum_move += visited[nx][ny]

    print('#{} {}'.format(tc, sum_move))
    print(arr)
    print(visited)