from collections import deque

N = int(input())
lst = [[] for _ in range(N+1)]
res = [0]*(N+1)
candi = [1]
candi = deque(candi)

for _ in range(N-1):
    s, e = map(int, input().split())
    lst[s].append(e)
    lst[e].append(s)

while candi:
    now = candi.popleft()
    for i in lst[now]:
        if i == res[now]:
            continue
        res[i] = now
        candi.append(i)

for i in range(2, N+1):
    print(res[i])