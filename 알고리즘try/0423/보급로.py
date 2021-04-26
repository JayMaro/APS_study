import heapq


def dijkstra(r, c):
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = 1
    q = [(0, r, c)]
    heapq.heapify(q)
    while q:
        dist, x, y = heapq.heappop(q)
        if val_arr[x][y] < dist:
            continue
        visited[x][y] = 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                if visited[xx][yy] == 0 and map_arr[xx][yy] + dist < val_arr[xx][yy]:
                    val_arr[xx][yy] = map_arr[xx][yy] + dist
                    heapq.heappush(q, (val_arr[xx][yy], xx, yy))


for tc in range(1, 1+int(input())):
    N = int(input())
    map_arr = [list(map(int, list(input()))) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    val_arr = [[1000000]*N for _ in range(N)]
    val_arr[0][0] = 0
    dijkstra(0, 0)
    print('#{} {}'.format(tc, val_arr[N-1][N-1]))

