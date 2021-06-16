def check(x):
    global n
    while True:
        if x > n:
            s.append(n)
            res.append('+')
            n += 1
        elif x == n:
            s.append(n)
            res.append('+')
            s.pop()
            res.append('-')
            n += 1
            return True
        else:
            if s[-1] == x:
                s.pop()
                res.append('-')
                return True
            else:
                return False


N = int(input())
lst = [int(input()) for _ in range(N)]
s = []
res = []
n = 1
flag = True
for i in range(len(lst)):
    x = lst[i]
    if not check(x):
        flag = False
        break

if flag:
    for i in res:
        print(i)
else:
    print('NO')

