def check(k, sum_val):
    global min_val, flag
    if flag == 1:
        return
    if sum_val >= min_val:
        return
    if k == lst_len:
        if B < sum_val:
            min_val = sum_val
        elif B == sum_val:
            min_val = B
            flag = 1
        return

    check(k+1, sum_val + lst[k])
    check(k+1, sum_val)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    lst_len = len(lst)
    min_val = 2000000
    flag = 0
    check(0, 0)
    print('#{} {}'.format(tc, min_val-B))