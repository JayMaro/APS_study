def color(arr, wb, br):
    global min_val
    cnt = 0
    for i in range(wb):
        for j in range(M):
            if arr[i][j] != 'W':
                cnt += 1
                if cnt > min_val:
                    return cnt
    for i in range(wb, br):
        for j in range(M):
            if arr[i][j] != 'B':
                cnt += 1
                if cnt > min_val:
                    return cnt
    for i in range(br, N):
        for j in range(M):
            if arr[i][j] != 'R':
                cnt += 1
                if cnt > min_val:
                    return cnt
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_val = 999999
    for k in range(1, N-1):
        for l in range(k+1, N):
            min_val = min(min_val, color(arr, k, l))
    print('#{} {}'.format(tc, min_val))
