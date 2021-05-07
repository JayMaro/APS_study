def check(level):
    if level == 0:
        sum_arr[0][0] = arr[0][0]
    if level == N:
        return
    for i in range(level+1):
        v1, v2 = 0, 0
        if i-1 >= 0:
            v1 = sum_arr[level-1][i-1]
        if i != level:
            v2 = sum_arr[level-1][i]
        sum_arr[level][i] = arr[level][i] + max(v1, v2)
    check(level+1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sum_arr = [[0]*i for i in range(1, N+1)]
check(0)
print(max(sum_arr[-1]))

