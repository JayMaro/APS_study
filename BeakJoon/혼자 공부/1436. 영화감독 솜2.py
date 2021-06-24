N = int(input())
num_lst = [0]*10001
i = 1
num = 666
while num_lst[N] == 0:
    string_num = str(num)
    if string_num.count('666') > 0:
        num_lst[i] = num
        i += 1
    num += 1
print(num_lst[N])