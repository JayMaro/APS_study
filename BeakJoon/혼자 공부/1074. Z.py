def check(x, y, n, r, c, cnt):
    if n == 1:
        return cnt

    if r < x+n // 2:
        if c < y+n // 2:
            return check(x, y, n // 2, r, c, cnt)
        else:
            return check(x, y+n // 2, n // 2, r, c, cnt + (n//2)**2)
    else:
        if c < y + n // 2:
            return check(x+n // 2, y, n // 2, r, c, cnt + 2*(n//2)**2)
        else:
            return check(x+n // 2, y+n // 2, n // 2, r, c, cnt + 3*(n//2)**2)


N, r, c = map(int, input().split())
print(check(0, 0, 2**N, r, c, 0))
