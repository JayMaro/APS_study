# def dfs(node):
#     stack = [node]
#     visited[node] = 1
#     length = 0
#     while stack:
#         now = stack.pop()
#         length += 1
#         for g in graph[now]:
#             if visited[g] == 0:
#                 visited[g] = 1
#                 stack.append(g)
#     return length


def dfs(node, length):
    global res
    if length > res:
        res = length
    visited[node] = 1
    for g in graph[node]:
        if visited[g] == 0:
            dfs(g, length+1)
            visited[g] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    res = 0
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1, N+1):
        visited = [0]*(N+1)
        dfs(i, 1)
    print('#{} {}'.format(tc, res))
