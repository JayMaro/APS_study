from collections import deque

N, M = map(int, input().split())
lst = [set() for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    lst[s].add(e)
    lst[e].add(s)


def bfs(v, target):
    Q = [(v, 0)]
    Q = deque(Q)
    visited = [0]*(N+1)
    while Q:
        x, length = Q.popleft()
        if x == target:
            return length
        for node in lst[x]:
            if visited[node] == 0:
                visited[node] = 1
                Q.append((node, length+1))


res = [0] * (N+1)
min_people = 0
min_val = 10000
for i in range(1, N+1):
    for j in range(1, N + 1):
        res[i] += bfs(i, j)

for i in range(1, N+1):
    if res[i] < min_val:
        min_val = res[i]
        min_people = i
print(min_people)