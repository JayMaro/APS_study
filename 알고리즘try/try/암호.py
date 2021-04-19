import sys
sys.stdin = open("input.txt", "r")

def check(string):
    if string == '0001101':
        return 0
    elif string == '0011001':
        return 1
    elif string == '0010011':
        return 2
    elif string == '0111101':
        return 3
    elif string == '0100011':
        return 4
    elif string == '0110001':
        return 5
    elif string == '0101111':
        return 6
    elif string == '0111011':
        return 7
    elif string == '0110111':
        return 8
    elif string == '0001011':
        return 9


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    password = ''
    check_lst = ['0'] * M
    res = []
    odd, even = 0, 0
    for _ in range(N):
        tmp = list(input())
        if tmp != check_lst:
            pass_lst = tmp

    for i in range(len(pass_lst) - 1, -1, -1):
        if pass_lst[i] == '1':
            password = pass_lst[i - 55:i + 1]
            break

    for i in range(8):
        word = ''.join(password[7 * i:7 * (i + 1)])
        res.append(check(word))

    for i in range(8):
        if i % 2 == 0:
            odd += res[i]
        else:
            even += res[i]

    if (odd*3 + even) % 10 == 0:
        print('#{} {}'.format(tc, odd+even))
    else:
        print('#{} {}'.format(tc, 0))

