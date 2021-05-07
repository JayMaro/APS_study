import heapq


def dijkstra(start):
    q = [(0, start)]
    heapq.heapify(q)
    v = [0] * (V+1)
    while q:
        dist, node = heapq.heappop(q)
        if v[node] == 1 or dist_lst[node] < dist:
            continue
        v[node] = 1
        for i in range(len(arr[node])):
            to_w, to_v = arr[node][i]
            if v[to_v] == 0:
                distance = to_w + dist
                if dist_lst[to_v] > distance:
                    dist_lst[to_v] = distance
                    heapq.heappush(q, (distance, to_v))


V, E = map(int, input().split())
K = int(input())
arr = [[]*(V+1) for _ in range(V+1)]
dist_lst = [2000000] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))
dist_lst[K] = 0
dijkstra(K)
for i in range(1, len(dist_lst)):
    if dist_lst[i] == 2000000:
        print('INF')
    else:
        print(dist_lst[i])
