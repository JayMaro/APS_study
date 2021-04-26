from collections import deque
import heapq

def dijkstra(x):
    q = [(x, 0)]
    heapq.heapify(q)
    while q:
        dist, now = heapq.heappop(q)
        for next_node in graph[now]:
            if w_lst[next_node[0]] > w_lst[now] + next_node[1]:
                w_lst[next_node[0]] = w_lst[now] + next_node[1]
                heapq.heappush(q, (w_lst[next_node[0]], next_node[0]))


for tc in range(1, 1+int(input())):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    w_lst = [100000] * (N+1)
    road_lst = [tuple(map(int, input().split())) for _ in range(E)]
    for road in road_lst:
        s, e, w = road
        graph[s].append([e, w])
    w_lst[0] = 0
    dijkstra(0)
    print('#{} {}'.format(tc, w_lst[-1]))

