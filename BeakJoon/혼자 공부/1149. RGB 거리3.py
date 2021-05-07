# 성공 DP로 푸니 역시 빠르다.

def check():
    for i in range(3):
        res[0][i] = arr[0][i]
    idx = 1
    while idx < N:
        for i in range(3):
            for j in range(3):
                if i != j:
                    tmp = res[idx-1][j] + arr[idx][i]
                    if tmp < res[idx][i]:
                        res[idx][i] = tmp
        idx += 1



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = [[10000000]*3 for _ in range(N)]
check()
print(min(res[-1]))
