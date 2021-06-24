lst = [0]*1006
lst[1] = 1
lst[2] = 3
N = int(input())
for i in range(3, N+1):
    lst[i] = lst[i-1] + 2*lst[i-2]
print(lst[N]%10007)