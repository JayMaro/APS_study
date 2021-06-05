for tc in range(int(input())):
    N = int(input())
    lst_0 = [0]*50
    lst_1 = [0]*50
    lst_0[0] = 1
    lst_1[1] = 1


    def fibonacci(N, lst):
        for i in range(N):
            lst[i+2] = lst[i]+lst[i+1]
        return lst[N]


    print(fibonacci(N, lst_0), fibonacci(N, lst_1))
