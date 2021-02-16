def func(n):
    if n == 1:
        return 1
    if n%2 == 1:
        print(n)
        return func(3*n + 1)
    else:
        print(n)
        return func(int(n/2))

print(func(3))
