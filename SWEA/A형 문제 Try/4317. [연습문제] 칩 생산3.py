# 음... 이건 올바른 풀이가 아닌것 같습니다
# 다른 분들 코드를 참고하세요!!ㅠ

def deepcopy(arr):
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = arr[i][j]
    return tmp


def bfs_check(x, y, tmp):
    global cnt
    if x+1 < N and y+1 < M:
        if tmp[x][y] == 0 and tmp[x+1][y] == 0 and tmp[x][y+1] == 0 and tmp[x+1][y+1] == 0:
            tmp[x][y] = tmp[x+1][y] = tmp[x][y+1] = tmp[x+1][y+1] = 1
            cnt += 1



def bfs(r, c):
    tmp = deepcopy(arr)
    q = [(r, c)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    v = [[0]*M for _ in range(N)]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<N and 0<=yy<M and v[xx][yy] == 0:
                v[xx][yy] = 1
                bfs_check(xx, yy ,tmp)
                q.append((xx, yy))

def check(x, y):
    global cnt
    if x + 1 < N and y + 1 < M:
        if tmp[x][y] == 0 and tmp[x + 1][y] == 0 and tmp[x][y + 1] == 0 and tmp[x + 1][y + 1] == 0:
            tmp[x][y] = tmp[x + 1][y] = tmp[x][y + 1] = tmp[x + 1][y + 1] = 1
            cnt += 1


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = deepcopy(arr)
    cnt = 0
    max_cnt = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            bfs(i, j)
            if cnt > max_cnt:
                max_cnt = cnt
    cnt = 0

    for i in range(N):
        for j in range(M):
            check(i, j)

    cnt1 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for i in range(N - 1, -1, -1):
        for j in range(M - 1, -1, -1):
            check(i, j)

    cnt2 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for i in range(N - 1, -1, -1):
        for j in range(M):
            check(i, j)

    cnt3 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for i in range(N):
        for j in range(M - 1, -1, -1):
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
        for i in range(N - 1, -1, -1):
            check(i, j)

    cnt6 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for j in range(M):
        for i in range(N - 1, -1, -1):
            check(i, j)

    cnt7 = cnt
    tmp = deepcopy(arr)
    cnt = 0

    for j in range(M - 1, -1, -1):
        for i in range(N):
            check(i, j)
    cnt8 = cnt

    print('#%d %d' % (tc + 1, max(cnt1, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8, max_cnt)))