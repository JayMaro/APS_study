def check(x, y, cnt, tmp):
    tmp += arr[x][y]
    if cnt == 7:
        res_lst.add(tmp)
        return

    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0 <= xx < 4 and 0 <= yy < 4:
            check(xx, yy, cnt+1, tmp)


T = int(input())
for tc in range(1, 1+T):
    arr = [input().split() for _ in range(4)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res_lst = set()
    for i in range(4):
        for j in range(4):
            check(i, j, 1, '')
    print('#{} {}'.format(tc, len(res_lst)))