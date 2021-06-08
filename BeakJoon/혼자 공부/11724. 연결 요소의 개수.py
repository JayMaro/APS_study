def find(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    if find(x) != find(y):
        p[find(x)] = find(y)


N, M = map(int, input().split())
p = list(range(N+1))
for _ in range(M):
    s, e = map(int, input().split())
    union(s, e)

S = set()
for i in range(1, N+1):
    S.add(find(i))

print(len(S))

