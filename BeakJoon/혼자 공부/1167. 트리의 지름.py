# 한 점에서 최장거리의 점을 구한 후
# 그 점에서 최장거리를 구하면 그것이 트리의 지름!
# 알아두자

from collections import deque


def dfs(x, sum_val):
    global max_val, last_idx
    v[x] = 1

    for node in lst[x]:
        if v[node[0]] == 0:
            v[node[0]] = 1
            dfs(node[0], sum_val + node[1])
            v[node[0]] = 0
    if sum_val > max_val:
        max_val = sum_val
        last_idx = x
    v[x] = 0


N = int(input())
v = [0]*(N+1)
lst = [[]*(N+1) for _ in range(N+1)]

for _ in range(N):
    input_lst = deque(map(int, input().split()))
    idx = input_lst.popleft()
    input_lst.pop()
    for i in range(0, len(input_lst), 2):
        lst[idx].append((input_lst[i], input_lst[i+1]))

res = 0
last_idx = 1
for _ in range(2):
    max_val = 0
    first_idx = last_idx
    dfs(last_idx, 0)
    res = max_val
print(res)