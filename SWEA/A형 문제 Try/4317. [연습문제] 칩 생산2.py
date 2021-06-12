def deepcopy(arr):
    tmp = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmp[i][j] = arr[i][j]
    return tmp


def check(x, y, tmp):
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
                check(xx, yy ,tmp)
                q.append((xx, yy))


for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            bfs(i, j)
            if cnt > max_cnt:
                max_cnt = cnt


    print('#%d %d' % (tc+1, max_cnt))