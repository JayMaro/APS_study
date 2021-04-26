import heapq


def prim(start):
    q = [(0, start)]
    heapq.heapify(q)
    cnt = 0
    sum_val = 0
    while q:
        val, nxt = heapq.heappop(q)
        if visited[nxt] == 1:
            continue
        visited[nxt] = 1
        sum_val += val
        cnt += 1
        if cnt == N:
            return sum_val
        for i in range(N):
            heapq.heappush(q, (map_arr[nxt][i], i))


for tc in range(1, 1+int(input())):
    N = int(input())
    # 각 섬의 좌표 리스트
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())
    map_arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            x1, x2 = x_lst[i], x_lst[j]
            y1, y2 = y_lst[i], y_lst[j]
            map_arr[i][j] = (x1-x2)**2 + (y1-y2)**2
            map_arr[j][i] = (x1-x2)**2 + (y1-y2)**2
    visited = [0]*N
    print('#{} {}'.format(tc, int(round(prim(0) * E))))

