from collections import deque

N, K = map(int, input().split())
def check():
    q = deque()
    q.append((N, 0))
    v = [0]*100001
    v[N] = 1
    while q:
        x, t = q.popleft()
        if x == K:
            return t
        if x+1 < 100001 and v[x+1] == 0:
            q.append((x+1, t+1))
            v[x + 1] = 1
        if x-1 >= 0 and v[x-1] == 0:
            q.append((x-1, t+1))
            v[x - 1] = 1
        if 0<= 2*x <= 100000 and v[2*x] == 0:
            q.append((2*x, t+1))
            v[2 * x] = 1

print(check())