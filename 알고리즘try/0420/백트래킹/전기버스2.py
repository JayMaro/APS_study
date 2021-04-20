def check(k, battery, cnt):
    global min_cnt
    if battery < 0 or cnt >= min_cnt:
        return

    if k == N - 1:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    check(k + 1, battery_lst[k] - 1, cnt+1)
    check(k + 1, battery - 1, cnt)


T = int(input())
for tc in range(1, T+1):
    input_lst = list(map(int, input().split()))
    N = input_lst[0]
    battery_lst = input_lst[1:]
    min_cnt = 1000
    check(0, 0, 0)
    print('#{} {}'.format(tc, min_cnt-1))