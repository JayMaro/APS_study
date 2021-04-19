T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_taste = -1
    for i in range(1<<N):
        cal_sum, taste_sum = 0, 0
        for j in range(N):
            if i & (1<<j):
                cal_sum += arr[j][1]
                taste_sum += arr[j][0]
                if cal_sum > L:
                    break
                else:
                    if taste_sum > max_taste:
                        max_taste = taste_sum

    print('#{} {}'.format(t, max_taste))