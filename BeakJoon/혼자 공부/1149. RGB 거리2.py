# 메모리 초과

def check(idx, lst, color):
    global res

    if idx == N:
        res.append(lst[:])
        return

    for i in range(3):
        if color == i:
            continue
        lst.append(i)
        check(idx+1, lst, i)
        lst.pop()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = []
min_val = 1000*1000*10
check(0, [], -1)
for result in res:
    sum_val = 0
    for i in range(N):
        if sum_val > min_val:
            break
        sum_val += arr[i][result[i]]
    if sum_val < min_val:
        min_val = sum_val
print(min_val)