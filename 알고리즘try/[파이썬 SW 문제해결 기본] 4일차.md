# [파이썬 S/W 문제해결 기본] 4일차

## 4869. 종이붙이기

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    n = N//10
    res = [1]
    # 원래수를 2곱하고 1을 뺀 수와 2곱하고 1을 더한 수가 반복된다
    for i in range(1,n+1):
        res.append(2*res[i-1] + (-1)**i)
    print('#{} {}'.format(t, res[-1]))
```

## 4866. 괄호검사

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    bracket = []
    flag = 1
    for char in str1:
        # 여는 괄호가 나오면 스택에 저장한다
        if char == '(' or char == '{':
            bracket.append(char)
        # 스택이 비어있지 않고 닫는 괄호가 나오면 스택에서 추출한 값과 비교한다
        elif bracket != [] and char == ')':
            x = bracket.pop()
            if x != '(':
                flag = 0
        elif bracket != [] and char == '}':
            x = bracket.pop()
            if x != '{':
                flag = 0
        # 스택이 비어있는 상태에서 닫는 괄호가 나온다면 0을 반환한다
        elif char == ')' or char == '}':
            flag = 0
    if bracket != []:
        flag = 0
    print('#{} {}'.format(t, flag))
```



## 4871. 그래프 경로

```python
def dfs(s, g):
    # 스택을 정의한다
    stack_s = []
    # 스택에 시작 노드가 갈 수 있는 노드들을 더한다
    stack_s += graph_dict[s]
    # 시작 노드를 방문 목록에 넣는다
    visited.append(s)
    # 스택이 비어있지 않을 때까지 반복한다
    while stack_s != []:
        # 스택에서 pop한 값을 C에 저장한다
        C = stack_s.pop()
        # 만약 C가 목표 노드와 같다면 1을 반환한다
        if C == g:
            return 1
        # 만약 C가 방문 목록에 없다면 추가하고
        # C가 갈 수 있는 노드들을 스택에 추가한다
        if C not in visited:
            visited.append(C)
            stack_s += graph_dict[C]
    # 만약 모두 반복했음에도 끝내지 못했다면 0을 반환한다.
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    visited = []
    # 그래프를 딕셔너리로 정리했다.
    graph_dict = {key: [] for key in range(V+1)}
    # 노드에서 갈 수 있는 곳만을 value의 리스트에 추가한다
    for i in range(E):
        start, end = map(int, input().split())
        graph_dict[start].append(end)
    S, G = map(int, input().split())

    print('#{} {}'.format(t, dfs(S, G)))
```



## 4873. 반복문자 지우기

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    # 스택에 idx err를 방지하기 위한 padding인 0을 추가한다
    stack = [0]
    # 스택에 str1의 문자들을 추가하고 같은 문자가 연속으로 들어온다면
    # pop을 통해 제거한다
    for char in str1:
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    print('#{} {}'.format(t, len(stack)-1))
```

