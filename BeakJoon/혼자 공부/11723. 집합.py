import sys
input = sys.stdin.readline

S = set()
N = int(input())

for _ in range(N):
    commend_lst = input().split()
    if commend_lst[0] == 'add':
        S.add(int(commend_lst[1]))
    elif commend_lst[0] == 'remove' and int(commend_lst[1]) in S:
        S.remove(int(commend_lst[1]))
    elif commend_lst[0] == 'check':
        if int(commend_lst[1]) in S:
            print(1)
        else:
            print(0)
    elif commend_lst[0] == 'toggle':
        if int(commend_lst[1]) in S:
            S.remove(int(commend_lst[1]))
        else:
            S.add(int(commend_lst[1]))
    elif commend_lst[0] == 'all':
        S = set(range(1, 21))
    elif commend_lst[0] == 'empty':
        S = set()

