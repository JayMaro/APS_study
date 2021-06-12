import pprint

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
val = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        top = 1000000
        left = 1000000
        if i - 1 >= 0:
            top = val[i-1][j]
        if j - 1 >= 0:
            left = val[i][j-1]
        val[i][j] = min(top, left) + arr[i][j]
pprint.pprint(val)
print(val[-1][-1])

