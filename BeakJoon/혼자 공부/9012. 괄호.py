T = int(input())
for tc in range(1, T+1):
    ps = input()
    flag = 1
    s = []
    for i in range(len(ps)):
        if ps[i] == ')':
            if s != []:
                s.pop()
            else:
                flag = 0
                break
        else:
            s.append('(')
    if s != []:
        flag = 0
    if flag:
        print('YES')
    else:
        print('NO')
