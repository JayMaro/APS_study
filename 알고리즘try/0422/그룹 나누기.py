def union(a, b):
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        p[p_a] = p_b
    return


def find(num):
    while num != p[num]:
        num = p[num]
    return num


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    p = list(range(N+1))
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        union(lst[i], lst[i+1])
    res_lst = []
    for i in range(1, N+1):
        if p[i] == i:
            res_lst.append(i)

    print('#{} {}'.format(tc, len(res_lst)))
