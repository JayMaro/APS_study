# [파이썬 SW 문제해결 기본] 6일차

## 노드의 거리

```python
def bfs(s, e):
    # 시작점의 거리는 0
    visited[s] = 0
    # 큐에 시작점 추가
    q = [s]
    # 거리는 1부터 시작
    distance = 1
    while q:
        # q의 길이만큼 반복
        for i in range(len(q)):
            # dequeue
            v = q.pop(0)
            # v의 인접 node 중 방문이 되지 않았다면
            # 방문확인 리스트에 시작점과의 거리를 저장 후
            # queue에 추가
            for j in graph[v]:
                if visited[j] == -1:
                    visited[j] = distance
                    q.append(j)
                # 만약 j가 끝점이라면 거리를 반환
                if j == e:
                    return distance
        distance += 1
    # 만약 끝점으로 갈 수 없다면 0을 반환
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 인접 딕셔너리
    graph = {key: [] for key in range(1, V+1)}
    # 방문확인 리스트
    visited = [-1] * (V+1)
    # 간선의 수만큼 인접 딕셔너리를 추가
    for i in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    # 시작점과 끝점 입력받음
    start, end = map(int, input().split())
    # bfs한 결과를 반환
    print('#{} {}'.format(tc, bfs(start,end)))
```



## 미로의 거리

```python
def bfs(arr, r, c):
    # 시작점을 1로 바꾸어 방문확인
    arr[r][c] = 1
    # 최초의 거리는 0부터 시작
    distance = 0
    # queue에 시작점의 좌표와 거리를 추가
    q = [[r, c, 0]]
    while q:
        # q의 길이만큼 반복한 이후 distance에 1을 더해 거리의 증가를 표현
        for i in range(len(q)):
            # dequeue
            v = q.pop(0)
            # 현재 좌표를 할당
            r, c = v[0], v[1]
            # 상 우 하 좌 모두 확인
            for j in range(4):
                r += dr[j]
                c += dc[j]
                # 만약 0이라면 방문확인 후 q에 좌표와 거리 추가
                if arr[r][c] == 0:
                    q.append([r, c, distance])
                    arr[r][c] = 1
                # 만약 도착했다면 그곳의 좌표와 거리를 반환
                if arr[r][c] == 3:
                    return r, c, distance
                r -= dr[j]
                c -= dc[j]
        distance += 1
    # 3을 찾지 못했다면 모두 0을 반환
    return 0, 0, 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 상 우 하 좌 순으로 확인하는 delta 값
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # 위아래 양 옆에 padding을 추가해 index error 방지
    arr = [[1]+[int(i) for i in input()]+[1] for _ in range(N)]
    arr = [[1] * (N + 2)] + arr + [[1] * (N + 2)]
    # 시작점의 위치를 찾음
    for i in range(len(arr)):
        if 2 in arr[i]:
            c = arr[i].index(2)
            r = i
    # bfs 실행 후 가장 마지막 값인 거리를 출력
    print('#{} {}'.format(tc, bfs(arr, r, c)[2]))
```



## 피자 굽기

```python
def pizza():
    while True:
        # 피자의 번호와 치즈를 화덕에서 꺼냄
        n, c = q.pop(0)
        # 다시 화덕에 넣고 치즈를 반으로 줄임
        q.append([n, c//2])
        # 만약 반으로 줄인 치즈가 0이라면 반환
        if c//2 == 0:
            return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 피자의 번호와 치즈를 함께 저장
    lst = [[idx, int(i)] for idx, i in enumerate(input().split(), 1)]
    q = []
    # 화덕의 크기만큼 피자에서 빼내어 넣음
    for i in range(N):
        q.append(lst.pop(0))
    # 화덕안의 피자가 1개가 남을때까지 반복
    while len(q) != 1:
        # 피자 실행
        pizza()
        # return이 되었다면 화덕안 마지막 피자의 치즈가 0이므로 제거
        q.pop()
        # 만약 피자가 남아있다면 화덕에 추가
        if lst:
            q.append(lst.pop(0))
    print('#{} {}'.format(tc, q[0][0]))
```



## 회전

```python
# enqueue와 dequeue를 같이 실행하는 함수
def rotate_queue(lst):
    x = lst.pop(0)
    lst.append(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # 지정된 횟수만큼 rotate함수를 실행 후 제일 처음 값을 출력
    for i in range(M):
        rotate_queue(lst)
    print('#{} {}'.format(tc, lst[0]))
```

