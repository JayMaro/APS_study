def union(x, y):
    if find(x) != find(y):
        p[find(x)] = find(y)


def find(x):
    while x != p[x]:
        x = p[x]
    return x


N = int(input())
M = int(input())
p = [i for i in range(N+1)]
cnt = 0
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N+1):
    p[i] = find(i)
    if p[i] == p[1]:
        cnt += 1

print(cnt-1)