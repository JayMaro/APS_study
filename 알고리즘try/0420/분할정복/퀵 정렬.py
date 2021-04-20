def quick_sort(lst, l, r):
    if l >= r:
        return
    p = lst[l]
    i, j = l+1, r
    while i <= j:
        while i <= j and p >= lst[i]:
            i += 1
        while i <= j and p <= lst[j]:
            j -= 1
        # if lst[i] <= p:
        #     i += 1
        #     continue
        # if lst[j] >= p:
        #     j -= 1
        #     continue
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[j], lst[l] = lst[l], lst[j]

    quick_sort(lst, l, j-1)
    quick_sort(lst, j+1, r)


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    num_lst = list(map(int, input().split()))
    quick_sort(num_lst, 0, N-1)
    print('#{} {}'.format(tc, num_lst[N//2]))