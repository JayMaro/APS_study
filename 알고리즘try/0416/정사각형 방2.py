def check(x, y, cnt):
    global res
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < N and 0 <= yy < N:
            if arr[xx][yy] == arr[x][y]+1:
                return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    link_lst = [0]*(N**2)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = [0, 0]
    cnt = 1
    for i in range(N):
        for j in range(N):
            if check(i, j, 1):
                link_lst[arr[i][j]] = 1
    for i in range(len(link_lst)):
        if link_lst[i] == 1:
            if cnt == 1:
                tmp = i
            cnt += 1
            if cnt > res[1]:
                res = [tmp, cnt]
        else:
            cnt = 1
    print('#{}'.format(tc), end=' ')
    print(*res)