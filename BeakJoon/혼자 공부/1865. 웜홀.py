import heapq


def dijkstra(start):
    q = [(0, start)]
    heapq.heapify(q)
    while q:
        dist, node = heapq.heappop(q)
        if v[node] == 1 or dist_lst[node] < dist:
            continue
        for i in range(len(arr[node])):
            to_node, to_w = arr[node][i]
            if v[to_node] == 0:
                distance = dist + to_w
                if distance < dist_lst[to_node]:
                    dist_lst[to_node] = distance
                    if dist_lst[start] < 0:
                        return 1
                    heapq.heappush(q, (distance, to_node))
    return 0


T = int(input())
for tc in range(T):
    N, M, W = map(int, input().split())
    arr = [[]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        S, E, T = map(int, input().split())
        arr[S].append((E, T))
        arr[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        arr[S].append((E, -T))

    res = 0
    for i in range(1, N+1):
        v = [0] * (N + 1)
        s = i
        dist_lst = [500 * 10001] * (N + 1)
        dist_lst[s] = 0
        res += dijkstra(s)
    if res:
        print('YES')
    else:
        print('NO')

