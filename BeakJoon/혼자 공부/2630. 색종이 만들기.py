import copy


def check(arr):
    arr_len = len(arr)
    color = arr[0][0]
    for i in range(arr_len):
        for j in range(arr_len):
            if arr[i][j] != color:
                return 2
    return color


def divide(arr):
    arr_len = len(arr)
    now_len = arr_len//2
    tmp = [[0]*now_len for _ in range(now_len)]

    for i in range(now_len):
        for j in range(now_len):
            tmp[i][j] = arr[i+now_len][j+now_len]
    arr_lst.append(copy.deepcopy(tmp))
    for i in range(now_len):
        for j in range(now_len):
            tmp[i][j] = arr[i][j+now_len]
    arr_lst.append(copy.deepcopy(tmp))
    for i in range(now_len):
        for j in range(now_len):
            tmp[i][j] = arr[i+now_len][j]
    arr_lst.append(copy.deepcopy(tmp))
    for i in range(now_len):
        for j in range(now_len):
            tmp[i][j] = arr[i][j]
    arr_lst.append(copy.deepcopy(tmp))


N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
arr_lst = [array]
blue_cnt = 0
white_cnt = 0

while arr_lst:
    arr = arr_lst.pop()
    if check(arr) == 1:
        blue_cnt += 1
    elif check(arr) == 0:
        white_cnt += 1
    else:
        divide(arr)

print(white_cnt)
print(blue_cnt)



