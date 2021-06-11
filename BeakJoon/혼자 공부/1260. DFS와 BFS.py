from collections import deque

N, M, V = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)
for i in range(1, N+1):
    lst[i].sort(reverse=True)

def dfs(v):
    S = [v]
    visited = [0] * (N+1)
    res = []
    while S:
        x = S.pop()
        if visited[x] == 1:
            continue
        visited[x] = 1
        res.append(x)
        for node in lst[x]:
            if visited[node] == 0:
                S.append(node)
    return res


def bfs(v):
    Q = [v]
    Q = deque(Q)
    visited = [0] * (N+1)
    res = []
    while Q:
        x = Q.popleft()
        if visited[x] == 1:
            continue
        visited[x] = 1
        res.append(x)
        for node in lst[x]:
            if visited[node] == 0:
                Q.append(node)
    return res


print(*dfs(V))
for i in range(1, N+1):
    lst[i].sort()
print(*bfs(V))

