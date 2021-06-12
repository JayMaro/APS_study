lst = [1, 50, 1, -1, 1, 3, -5, 1, -15, 0, 100, 1, 1, 2]
memo = [0]*20
short_jump = 2
long_jump = 7


def jump(score, now):
    if memo[now] < score:
        memo[now] = score
    if short_jump+now < len(lst):
        jump(score + lst[short_jump+now], short_jump+now)
    if long_jump + now < len(lst):
        jump(score + lst[long_jump+now], long_jump+now)

def jump2(now):
    short_len, long_len = 0, 0
    if now - 2 > 0:
        short_len = lst[now] + memo[now-2]
    if now - 7 > 0:
        long_len = lst[now] + memo[now-7]
    memo[now] = max(short_len, long_len)


jump(0, 0)
print(memo)
memo = [0]*20
for i in range(len(lst)):
    jump2(i)
print(memo)

