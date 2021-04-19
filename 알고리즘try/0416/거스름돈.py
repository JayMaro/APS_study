T = int(input())
for tc in range(1, T+1):
    money = int(input())
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res_lst = [0, 0, 0, 0, 0, 0, 0, 0]
    idx = 0
    while True:
        res_lst[idx] = (money // money_lst[idx])
        money %= money_lst[idx]
        idx += 1
        if idx == 8:
            break
    print('#{}'.format(tc))
    print(*res_lst)