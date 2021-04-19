def check(x, y, cnt):
    global res
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < N and 0 <= yy < N:
            if arr[xx][yy] == arr[x][y]+1:
                check(xx, yy, cnt+1)
    else:
        if cnt > res[1]:
            res = [arr[i][j], cnt]
        elif cnt == res[1]:
            if arr[i][j] < res[0]:
                res = [arr[i][j], cnt]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = [0, 0]
    for i in range(N):
        for j in range(N):
            check(i, j, 1)
    print('#{}'.format(tc), end=' ')
    print(*res)