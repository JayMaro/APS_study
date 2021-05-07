T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    N_lst = input().split()
    M_lst = input().split()

    cnt = len(set(N_lst) & set(M_lst))
    print('#{} {}'.format(tc, cnt))