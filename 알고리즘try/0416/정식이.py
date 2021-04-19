T = int(input())
for tc in range(1, T+1):
    bin = list(input())
    tri = list(input())

    bin_lst = []
    tri_lst = []
    triple = ['0', '1', '2']
    for i in range(len(bin)):
        tmp = bin[:]
        if tmp[i] == '0':
            tmp[i] = '1'
        else:
            tmp[i] = '0'
        bin_lst.append(''.join(tmp))
    for i in range(len(tri)):
        tmp = tri[:]
        idx = triple.index(tmp[i])
        for j in range(idx+1, idx+3):
            tmp[i] = triple[j%3]
            tri_lst.append(''.join(tmp))
    for bin_num in bin_lst:
        for tri_num in tri_lst:
            if int(bin_num, 2) == int(tri_num, 3):
                print('#{} {}'.format(tc, int(bin_num, 2)))
                break
