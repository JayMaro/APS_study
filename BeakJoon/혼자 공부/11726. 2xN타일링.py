N = int(input())
def fibo(n):
    lst = [0] * 10000
    lst[1] = 1
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] = (lst[i-1] + lst[i-2])
    return lst[n]
print(fibo(N) % 10007)