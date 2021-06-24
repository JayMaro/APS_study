N = int(input())
num_lst = [0]*10001
i = 1
num = 666
while num_lst[N] == 0:
    flag = 0
    tmp = num
    while True:
        if tmp % 10 == 6:
            flag += 1
            tmp //= 10
            if flag == 3:
                num_lst[i] = num
                i += 1
                break
        else:
            flag = 0
            tmp //= 10
            if tmp == 0:
                break
    num += 1
print(num_lst[N])

