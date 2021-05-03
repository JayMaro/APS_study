from collections import deque


def check(r, c):
    global max_val
    q = [(r, c, map_arr[0][0])]
    q = deque(q)
    while q:
        x, y, string = q.popleft()
        string_set.add(string)
        max_val = max(len(string), max_val)
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and map_arr[xx][yy] not in string:
                if string + map_arr[xx][yy] in string_set:
                    continue
                q.append((xx, yy, string + map_arr[xx][yy]))


N, M = map(int, input().split())
map_arr = [list(input()) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
string_set = set()
max_val = 0
check(0, 0)
print(max_val)









