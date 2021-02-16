def sum_list(data):
    if len(data) == 1:
        return data[0]
    elif len(data) > 1:
        return sum_list(data[:-1]) + data[-1]

print(sum_list([1,2,3,4,5,6,7,8,9,10,]))