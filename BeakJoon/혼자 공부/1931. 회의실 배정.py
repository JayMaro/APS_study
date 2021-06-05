N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))
now = 0
cnt = 0
for s, e in lst:
    if s >= now:
        now = e
        cnt += 1
print(cnt)