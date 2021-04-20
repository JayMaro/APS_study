def check(i, sum_val, cnt):
    global min_val
    if sum_val >= min_val:
        return

    if cnt == N:
        if sum_val < min_val:
            min_val = sum_val
        return

    for j in range(N):
        if visited_col[j] == 0:
            visited_col[j] = 1
            check(i + 1, sum_val + arr[i][j], cnt+1)
            visited_col[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited_col = [0]*N
    min_val = 99999
    check(0, 0, 0)
    print('#{} {}'.format(tc, min_val))

