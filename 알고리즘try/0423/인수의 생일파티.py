import heapq


def dijkstra(start, lst, arr):
    q = [(0, start)]
    heapq.heapify(q)
    v = [0]*(N+1)
    while q:
        dist, nxt = heapq.heappop(q)
        v[nxt] = 1
        if dist > lst[nxt]:
            continue
        for i in range(1, N+1):
            if arr[nxt][i] != 0:
                distance = arr[nxt][i] + dist
                if v[i] == 0 and distance < lst[i]:
                    lst[i] = distance
                    heapq.heappush(q, (distance, i))


for tc in range(1, int(input())+1):
    # 1에서 N번까지의 집
    # 대상 위치는 X
    N, M, X = map(int, input().split())
    input_lst = [list(map(int, input().split())) for _ in range(M)]
    go_map_arr = [[0]*(N+1) for _ in range(N+1)]
    come_map_arr = [[0]*(N+1) for _ in range(N+1)]
    go_lst = [10000000]*(N+1)
    come_lst = [10000000]*(N+1)
    go_lst[X] = 0
    come_lst[X] = 0
    for inp in input_lst:
        x, y, c = inp
        go_map_arr[x][y] = c
    for i in range(N+1):
        for j in range(N+1):
            come_map_arr[i][j] = go_map_arr[j][i]
    dijkstra(X, go_lst, go_map_arr)
    dijkstra(X, come_lst, come_map_arr)
    res_lst = [0]*(N+1)
    for i in range(1, N+1):
        res_lst[i] = go_lst[i] + come_lst[i]
    print('#{} {}'.format(tc, max(res_lst)))

