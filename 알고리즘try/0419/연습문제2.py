lst = list(range(1, 11))


def power_set(n, k):
    sum10_lst = []
    for i in range(1<<n):
        sum_val = 0
        tmp = []
        for j in range(n):
            if i & (1<<j):
                sum_val += lst[j]
                tmp.append(lst[j])
                if sum_val > k:
                    break
        if sum_val == k:
            sum10_lst.append(tmp)
    return sum10_lst

print(power_set(len(lst), 10))

