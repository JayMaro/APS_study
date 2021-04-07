# [파이썬 SW문제해결 기본] - Tree



## subtree

```python
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 간선의 수 + 1 = 노드의 수
    # 노드의수 + 1 만큼 배열을 선언
    parent = [0]*(E+2)
    tree_lst = list(map(int, input().split()))
    # 서브 트리의 갯수를 저장할 변수
    cnt = 0
    # 2개씩 끊어서 불러옴
    for i in range(0, len(tree_lst), 2):
        # 먼저 오는 수가 부모
        par = tree_lst[i]
        # 뒤에 오는 수가 자식
        child = tree_lst[i+1]
        # index를 자식으로 value를 부모로 설정
        parent[child] = par


    # 서브 트리의 루트 노드를 q에 넣는다.
    q = [N]
    # BFS 처럼 탐색
    while q:
        # q에서 부모 노드를 pop
        node = q.pop(0)
        cnt += 1
        # 리스트를 돌면서 부모노드의 값이 node인 것이 있다면 q에 추가
        for i in range(len(parent)):
            if parent[i] == node:
                q.append(i)
    print('#{} {}'.format(tc, cnt))
```



## 이진탐색

```python
# 중위 순회를 하면 이진 탐색 트리에서 정렬이 되는 것을 이용

def in_order(start):
    global cnt
    if start*2 <= N:
        in_order(start*2)
    # 현재 노드에 숫자를 저장하고 1 증가
    tree[start] = cnt
    cnt += 1
    if start*2 + 1 <= N:
        in_order(start * 2 + 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 노드의 수 + 1만큼 배열 선언
    tree = [0]*(N+1)
    # 증가시키는 숫자를 저장할 변수
    cnt = 1
    # 중위 순회를 하면서 값을 지정
    in_order(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
```



## 이진 힙

```python
def insert_heap(num):
    global index
    tree[index] = num
    tmp = index
    while tmp:
        if tree[tmp // 2] > tree[tmp]:
            tree[tmp], tree[tmp//2] = tree[tmp//2], tree[tmp]
        tmp = tmp//2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 노드 수+1 만큼 배열 선언
    tree = [0]*(N+1)
    # 결과를 저장할 변수
    res = 0
    # 추가된 노드의 index를 저장할 변수
    index = 1
    # 결과값에 더할 index를 저장한 변수
    sum_index = N
    input_lst = list(map(int, input().split()))
    for i in input_lst:
        # 힙에 넣고 정렬한 다음 index를 1 증가
        insert_heap(i)
        index += 1
    # 부모 노드가 0이 될때까지 반복
    while sum_index:
        # 부모 노드를 구하고
        sum_index = sum_index // 2
        # 부모 노드의 값을 결과 값에 더함
        res += tree[sum_index]
    print('#{} {}'.format(tc, res))

```



## 노드의 합

```python
def make_tree(leaf_node):
    # 만약 오른쪽 값이 존재한다면
    if leaf_node + 1 <= N:
        tree[leaf_node//2] = tree[leaf_node] + tree[leaf_node+1]
    # 왼쪽 값만 존재한다면
    else:
        tree[leaf_node//2] = tree[leaf_node]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    # 노드 + 1 만큼 배열 선언
    tree = [0]*(N+1)
    # 리프 노드들에 값을 저장
    for _ in range(M):
        node, val = map(int, input().split())
        tree[node] = val
    # 리프노드들 부터 값을 채워감
    for i in range(N, 0, -1):
        # 반복을 피하기 위해 조건 설정
        if i % 2 == 0:
            make_tree(i)

    print('#{} {}'.format(tc, tree[L]))

```

