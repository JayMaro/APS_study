def deepcopy(arr):
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = arr[i][j]
    return tmp


def check(x, y):
    global cnt
    if x+1 < N and y+1 < M:
        if tmp[x][y] == 0 and tmp[x+1][y] == 0 and tmp[x][y+1] == 0 and tmp[x+1][y+1] == 0:
            tmp[x][y] = tmp[x+1][y] = tmp[x][y+1] = tmp[x+1][y+1] = 1
            cnt += 1


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = deepcopy(arr)
    cnt = 0
    for i in range(N):
        for j in range(M):
            check(i, j)

    cnt1 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            check(i, j)

    cnt2 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for i in range(N-1, -1, -1):
        for j in range(M):
            check(i, j)

    cnt3 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for i in range(N):
        for j in range(M-1, -1, -1):
            check(i, j)

    cnt4 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for j in range(M):
        for i in range(N):
            check(i, j)

    cnt5 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for j in range(M - 1, -1, -1):
        for i in range(N-1, -1, -1):
            check(i, j)

    cnt6 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for j in range(M):
        for i in range(N-1, -1, -1):
            check(i, j)

    cnt7 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for j in range(M - 1, -1, -1):
        for i in range(N):
            check(i, j)
    cnt8 = cnt

    print('#%d %d' % (tc+1, max(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8)))