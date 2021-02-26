# SWEA

## D4



### 5432. 쇠막대기 자르기

```python
T = int(input())
for t in range(1, T+1):
    pipe = input()
    # 현재 파이프 갯수
    pipe_cnt = 0
    # 총 갯수
    res = 0
    # 바로 닫히면 레이저
    # (가 생가면 pip 갯수 1 증가
    # )로 닫히면 pip 갯수 1 감소, 총 갯수 1 증가
	# ()가 생기면 pip 갯수만큼 총 갯수 증가
    i = 0
    while True:
        if pipe[i] == '(' and i+1 < len(pipe):
            if pipe[i+1] == ')':
                res += pipe_cnt
                i += 2
                continue
            else:
                pipe_cnt += 1
        if pipe[i] == ')':
            res += 1
            pipe_cnt -= 1
        i += 1
        if i == len(pipe):
            break
    print('#{} {}'.format(t, res))
```



### 3143. 가장 빠른 문자열 타이핑

```python
T = int(input())
for t in range(1, T+1):
    str_a, str_b = input().split()
    cnt = str_a.count(str_b)
    str_res = str_a.replace(str_b, '', cnt)
    cnt += len(str_res)

    print('#{} {}'.format(t, cnt))
```



### [S/W 문제해결 기본] 2일차 - Ladder1 -> 아래에서 부터 풀면 더 쉽게 풀 수 있다.

```python
for _ in range(10):
    N = int(input())
    ladder = []
    for _ in range(100):
        i_lst = list(map(int, input().split()))
        ladder.append(i_lst)
 
    # 첫번째 행의 숫자가 1일때 아래로 내려간다
    # 내려갈 때 양 옆 중에 1인 숫자가 생기면 이동한다
    # 마지막 행에 도착하면 그 수를 확인하고 2라면 그 인덱스를 출력한다.
 
    for i in range(100):
        x = 0
        k = i
 
        while ladder[x][k] == 1:
            x += 1
            right = False
            while k+1 <= 99:
                if ladder[x][k+1] == 1:
                    right = True
                    k += 1
                else:
                    break
 
            while k-1 >= 0 and right is False:
                if ladder[x][k-1] == 1:
                    k -= 1
                else:
                    break
 
            if x == 99:
                break
        if ladder[x][k] == 2:
            print(f'#{N}', end=' ')
            print(i)
            break
```



### 길찾기 -> dfs 이용

```python
def dfs():
    s = []
    s += graph[0]
    visited.append(0)

    while s != []:
        current = s.pop()
        if current == 99:
            return 1
        if current not in visited:
            visited.append(current)
            s += graph[current]
    else:
        return 0


for test_case in range(1, 11):
    T, E = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = {key: [] for key in range(100)}
    visited = []
    for i in range(0, E*2, 2):
        graph[lst[i]].append(lst[i+1])
    print('#{} {}'.format(T, dfs()))
```



### 창용 마을 무리의 개수 -> dfs 와 union find로 풀었지만 union find는 뭔가 엉성하다 다시 풀어보자

```python
def dfs(p):
    s = []
    visited.append(p)
    s += people[p]
    while s != []:
        v = s.pop()
        if v not in visited:
            visited.append(v)
            s += people[v]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    people = {key: [] for key in range(1,N+1)}
    visited = []
    cnt = 0
    for _ in range(M):
        p1, p2 = map(int, input().split())
        people[p1].append(p2)
        people[p2].append(p1)

    for i in range(1, N+1):
        if i not in visited:
            dfs(i)
            cnt += 1

    print('#{} {}'.format(t, cnt))
```

```python
def union(a, b):
    if find(a) == find(b):
        return
    else:
        parent[find(a)] = find(b)


def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    parent = {key: key for key in range(1, N+1)}
    res_lst = []
    for _ in range(M):
        p1, p2 = map(int, input().split())
        union(p1, p2)

    for key, value in parent.items():
        if key == value:
            res_lst.append(key)
    res = len(res_lst)

    print('#{} {}'.format(t, res))
```



### 자기 방 찾아가기 ->이건 진짜 개 못했다... 배열이 있다면 바로 배열로 생각하지 말고 카운팅 부터 생각해보자

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    uplst = [i for i in range(1, 400, 2)]
    downlst = [i for i in range(2, 401, 2)]
    check = [0 for i in range(200)]
    for i in range(N):
        a, b = map(int, input().split())
        s = min(a, b)
        e = max(a, b)
        if s % 2:
            start = uplst.index(s)
        else:
            start = downlst.index(s)
        if e % 2:
            end = uplst.index(e)
        else:
            end = downlst.index(e)
        for j in range(start, end+1):
            check[j] += 1
    print('#{} {}'.format(t, max(check)))
```



