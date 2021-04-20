def make_per(x):
    x = int(x)
    x /= 100
    return x


def check(i, mul_val):
    global res
    if mul_val <= res:
        return

    if i == N:
        if mul_val > res:
            res = mul_val
        return

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            check(i+1, mul_val * arr[i][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(make_per, input().split())) for _ in range(N)]
    visited = [0]*N
    res = 0
    check(0, 1)
    print('#{} {:0.6f}'.format(tc, res*100))
