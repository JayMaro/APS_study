lst = list(input())
binary_num = ''
for i in range(len(lst)):
    tmp = bin(int(lst[i], 16))[2:]
    while len(tmp) != 4:
        tmp = '0'+tmp
    binary_num += tmp
res = []
for i in range(0, len(binary_num)//7):
    res.append(int(binary_num[:7], 2))
    binary_num = binary_num[7:]
if binary_num:
    res.append(int(binary_num, 2))

print(*res)
