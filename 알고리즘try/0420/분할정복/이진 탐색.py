def binary_search(lst, pur):
    lidx = 0
    ridx = len(lst)-1
    flag = 0
    while lidx <= ridx:
        mid = (lidx + ridx) // 2
        if lst[mid] == pur:
            return True
        elif lst[mid] < pur:
            if flag != 'r':
                lidx = mid+1
                flag = 'r'
            else:
                return False
        else:
            if flag != 'l':
                ridx = mid-1
                flag = 'l'
            else:
                return False
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    cnt = 0
    for b in B:
        if binary_search(A, b):
            cnt += 1
    print('#{} {}'.format(tc, cnt))