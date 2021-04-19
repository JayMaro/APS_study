def show_me_the_money(cnt):
    global max_val
    lst_len = len(N)
    if cnt == C:
        tmp = int(''.join(N_lst))
        if tmp > max_val:
            max_val = tmp
        return

    for i in range(lst_len-1):
        for j in range(i+1, lst_len):
            N_lst[i], N_lst[j] = N_lst[j], N_lst[i]
            if (''.join(N_lst), cnt) not in visited:
                visited.add((''.join(N_lst), cnt))
                show_me_the_money(cnt+1)
            N_lst[i], N_lst[j] = N_lst[j], N_lst[i]


T = int(input())
for tc in range(1, T+1):
    N, C = input().split()
    C = int(C)
    max_val = 0
    visited = set()
    N_lst = list(N)
    show_me_the_money(0)
    print('#{} {}'.format(tc, max_val))
