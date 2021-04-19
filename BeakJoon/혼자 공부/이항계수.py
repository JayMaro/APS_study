

N, K = map(int, input().split())
res = 1
div = 1
for i in range(K):
    res *= (N-i)
for i in range(K):
    div *= (i+1)
print(res//div)
