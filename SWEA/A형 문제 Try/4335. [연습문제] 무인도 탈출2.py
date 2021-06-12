# 재귀 함수 사용
import time


def check(idx, x, y, total, number):
    global max_height

    x1, y1, h1 = y2, h2, x2 = h3, x3, y3 = arr[idx]
    total1, total2, total3 = 0, 0, 0
    if (x >= x1 and y >= y1) or (x >= y1 and y >= x1):
        total1 = total + h1
    if (x >= x2 and y >= y2) or (x >= y2 and y >= x2):
        total2 = total + h2
    if (x >= x3 and y >= y3) or (x >= y3 and y >= x3):
        total3 = total + h3
    max_total = max(total1, total2, total3)
    if max_total > max_height:
        max_height = max_total
    if max_total == 0:
        return
    if number == N-1:
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            if total1:
                check(i, x1, y1, total1, number+1)
            if total2:
                check(i, x2, y2, total2, number+1)
            if total3:
                check(i, x3, y3, total3, number+1)
            visited[i] = 0


for tc in range(int(input())):

    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    max_height = 0
    for i in range(N):
        visited[i] = 1
        check(i, 10000, 10000, 0, 1)
        visited[i] = 0
    print('#%d %d' % (tc+1, max_height))