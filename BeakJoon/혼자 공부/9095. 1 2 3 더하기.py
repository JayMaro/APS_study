T = int(input())
for tc in range(T):
    N = int(input())
    def f(N):
        lst = [0] * 13
        lst[1] = 1
        lst[2] = 2
        lst[3] = 4
        for i in range(4, N+1):
            lst[i] = lst[i-1] + lst[i-2] + lst[i-3]
        return lst[N]
    print(f(N))