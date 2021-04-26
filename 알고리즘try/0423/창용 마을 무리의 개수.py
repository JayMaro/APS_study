def union(x, y):
    p_x = find(x)
    p_y = find(y)
    if p_x != p_y:
        p[p_x] = p_y
    return


def find(x):
    while x != p[x]:
        x = p[x]
    return x


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    p = list(range(N+1))
    lst = [tuple(map(int, input().split())) for _ in range(M)]
    cnt = 0
    for li in lst:
        a, b = li
        union(a, b)
    for i in range(1, N+1):
        if find(i) == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))