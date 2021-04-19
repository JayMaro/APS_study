import pprint


def trail(x, y, flag):
    global max_length
    max_length = max(len(trail_road), max_length)
    height = arr[x][y]
    for i in range(4):
        x += dx[i]
        y += dy[i]
        if arr[x][y] < height and visited[x][y] == 0:
            visited[x][y] = 1
            trail_road.append([x, y])
            trail(x, y, flag)
            visited[x][y] = 0
            trail_road.pop()
        elif flag == 1 and visited[x][y] == 0 and height > 0 and arr[x][y]-K < height:
            move_height = arr[x][y]
            flag = 0
            arr[x][y] = height - 1
            visited[x][y] = 1
            trail_road.append([x, y])
            trail(x, y, flag)
            flag = 1
            arr[x][y] = move_height
            visited[x][y] = 0
            trail_road.pop()

        x -= dx[i]
        y -= dy[i]


def search(arr):
    max_num = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            max_num = max(max_num, arr[i][j])
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == max_num:
                high_position.append([i, j])


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[100]+list(map(int, input().split()))+[100] for _ in range(N)]
    arr = [[100]*(N+2)] + arr + [[100]*(N+2)]
    max_length = 0
    high_position = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0]*(N+2) for _ in range(N+2)]
    trail_road = []
    search(arr)
    for x, y in high_position:
        trail_road.append([x, y])
        visited[x][y] = 1
        trail(x, y, 1)
        visited[x][y] = 0
        trail_road.pop()
    print('#{} {}'.format(tc, max_length))

