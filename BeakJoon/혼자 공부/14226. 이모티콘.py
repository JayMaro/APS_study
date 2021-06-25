# 나중에 다시 풀어보자
from collections import deque

N = int(input())
s = [(0, 1, 0)]
s = deque(s)
v = []
while s:
    time, now, save = s.popleft()
    if now == N:
        break
    if (now, save) in v:
        continue
    v.append((now, save))
    t1, n1, s1 = time+1, now, now
    t2, n2, s2 = time+1, now+save, save
    t3, n3, s3 = time+1, now-1, save

    if (n1, s1) not in v and s1 <= 1000:
        s.append((t1, n1, s1))
    if (n2, s2) not in v and save != 0 and n2 <= 2000:
        s.append((t2, n2, s2))
    if (n3, s3) not in v and n3 > 0:
        s.append((t3, n3, s3))

print(time)