from collections import deque


def dijkstra(x, y):
    q = [(x, y)]
    q = deque(q)
    while q:
        n_x, n_y = q.popleft()
        height = height_arr[n_x][n_y]
        cost = cost_arr[n_x][n_y]
        for i in range(4):
            tmp_cost = cost
            xx = n_x + dx[i]
            yy = n_y + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                if height < height_arr[xx][yy]:
                    tmp_cost += height_arr[xx][yy] - height
                tmp_cost += 1
                if tmp_cost < cost_arr[xx][yy]:
                    cost_arr[xx][yy] = tmp_cost
                    q.append((xx, yy))


for tc in range(1, 1+int(input())):
    N = int(input())
    height_arr = [list(map(int, input().split())) for _ in range(N)]
    cost_arr = [[1000000000]*N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cost_arr[0][0] = 0
    dijkstra(0, 0)
    print('#{} {}'.format(tc, cost_arr[N-1][N-1]))