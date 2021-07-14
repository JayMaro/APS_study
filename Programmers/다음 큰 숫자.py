def solution(n):
    x = bin(n)[2:]
    idx = 0
    cnt_0 = 0
    cnt_1 = 0
    res = ''
    for i in range(len(x)-1, 0, -1):
        if x[i] == '1':
            cnt_1 += 1
        if x[i] == '0':
            cnt_0 += 1
        if x[i-1] == '0' and x[i] == '1':
            idx = i
            break
    if idx != 0:
        res = x[:i-1] + '10' + '0'*cnt_0 + '1'*(cnt_1-1)
    else:
        res = '10' + '0'*cnt_0 + '1'*cnt_1

    return int(res, 2)