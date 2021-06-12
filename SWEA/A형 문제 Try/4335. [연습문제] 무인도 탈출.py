# 재귀 함수 사용
def check(idx, x, y, total, number):
    global max_height
    x1, y1, h1 = y2, h2, x2 = h3, x3, y3 = arr[idx]
    if number == N:
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
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            if (x >= x1 and y >= y1) or (x >= y1 and y >= x1):
                check(i, x1, y1, total+h1, number+1)
            if (x >= x2 and y >= y2) or (x >= y2 and y >= x2):
                check(i, x2, y2, total+h2, number+1)
            if (x >= x3 and y >= y3) or (x >= y3 and y >= x3):
                check(i, x3, y3, total+h3, number+1)
            check(i, x, y, total, number+1)
            visited[i] = 0


def start():
    for k in range(N):
        visited[k] = 1
        idx = k
        x, y = 10000, 10000
        number = 1
        x1, y1, h1 = y2, h2, x2 = h3, x3, y3 = arr[idx]
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                if (x >= x1 and y >= y1) or (x >= y1 and y >= x1):
                    check(i, x1, y1, h1, number + 1)
                if (x >= x2 and y >= y2) or (x >= y2 and y >= x2):
                    check(i, x2, y2, h2, number + 1)
                if (x >= x3 and y >= y3) or (x >= y3 and y >= x3):
                    check(i, x3, y3, h3, number + 1)
                check(i, x, y, 0, number + 1)
                visited[i] = 0
        visited[k] = 0


for tc in range(int(input())):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    max_height = 0
    start()
    print(max_height)