N, M = map(int, input().split())
dud = set()
bo = set()
for _ in range(N):
    dud.add(input())
for _ in range(M):
    bo.add(input())
res = list(dud.intersection(bo))
res.sort()

print(len(res))
for name in res:
    print(name)