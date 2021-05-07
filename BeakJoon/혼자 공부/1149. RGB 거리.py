# 시간 초과

def check(idx, sum_val, color):
    global res
    if sum_val > res:
        return

    if idx == N:
        if sum_val < res:
            res = sum_val
        return

    for i in range(3):
        if color == i:
            continue
        sum_val += arr[idx][i]
        check(idx+1, sum_val, i)
        sum_val -= arr[idx][i]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 1000 * 1000 * 10
check(0, 0, -1)
print(res)