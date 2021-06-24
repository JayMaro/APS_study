def check(idx, sum_val, tmp):
    global flag, res
    if flag == 1:
        return
    if sum_val == 100 and len(tmp) == 7:
        flag = 1
        res = tmp[:]
    if sum_val > 100:
        return
    if idx == 9:
        return

    check(idx+1, sum_val + lst[idx], tmp+[lst[idx]])
    check(idx+1, sum_val, tmp)


lst = [int(input()) for _ in range(9)]
lst.sort()
flag = 0
res = []

check(0, 0, [])

for num in res:
    print(num)
