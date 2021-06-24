T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    x = max(N, M)
    y = min(N, M)
    GD = 1
    while True:
        if y == 1:
            break
        if x % y == 0:
            GD = y
            break
        else:
            x, y = y, x % y

    n = N // GD
    m = M // GD
    GM = n*m*GD
    print(GM)
