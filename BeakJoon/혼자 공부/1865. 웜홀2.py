from collections import deque


def dijkstra(start):
    q = [(0, start)]
    q = deque(q)
    while q:
        dist, node = q.popleft()
        for i in range(len(arr[node])):
            to_node, to_w = arr[node][i]
            distance = dist + to_w
            if distance < dist_lst[to_node]:
                dist_lst[to_node] = distance
                if dist_lst[start] < 0:
                    return 1
                q.append((distance, to_node))
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

    s = 1
    dist_lst = [500 * 10001] * (N + 1)
    dist_lst[s] = 0

    if dijkstra(s):
        print('YES')
    else:
        print('NO')

