# [파이썬 S/W 문제해결 기본] 5일차

## Forth -> /은 float형 주의

```python
T = int(input())
for tc in range(1, T+1):
    lst = input().split()
    # 연산자인지 판별하기 위한 리스트
    operator = ['+', '-', '*', '/']
    # 스택
    s = []
    # error 인지 아닌지 판별하는 flag
    error = False
    for i in lst:
        # 연산자가 아니라면 스택에 더하고 '.'이라면 마지막이므로 break
        if i not in operator:
            if i == '.':
                break
            s.append(int(i))
        # 연산자라면 스택안의 수가 2 이상인지 확인하고 연산
        else:
            if len(s) >= 2:
                num1 = s.pop()
                num2 = s.pop()
                if i == '+':
                    s.append(num2 + num1)
                if i == '-':
                    s.append(num2 - num1)
                if i == '*':
                    s.append(num2 * num1)
                if i == '/':
                    # 만약 0으로 나누게 된다면 error는 True 설정이후 break
                    if num1 == 0:
                        error = True
                        break
                    s.append(int(num2 / num1))
            # 스택안의 수가 2 미만이라면 error는 True
            else:
                error = True
                break

    # 모든 연산이 끝난 이후 스택에 2개 이상의 수가 남아있다면 error는 True
    if len(s) != 1:
        error = True
    else:
        res = s.pop()

    if error:
        print('#{} error'.format(tc))
    else:
        print('#{} {}'.format(tc, res))
```

## 토너먼트 카드게임 -> 재귀함수 리턴값 주의

```python
# 가위바위보 함수
# 비겼다면 수가 작은 값을 반환
def rcp(a, b):
    if a[1] == '1':
        if b[1] == '1':
            return min(a, b, key=lambda x: x[0])
        elif b[1] == '2':
            return b
        else:
            return a
    elif a[1] == '2':
        if b[1] == '2':
            return min(a, b, key=lambda x: x[0])
        elif b[1] == '3':
            return b
        else:
            return a
    else:
        if b[1] == '3':
            return min(a, b, key=lambda x: x[0])
        elif b[1] == '1':
            return b
        else:
            return a


def winner(lst):
    # 리스트의 길이가 1이라면 그 값을 반환
    if len(lst) == 1:
        return lst[0]
    else:
        # 전반부와 후반부로 나눈 후 다시 함수에 대입
        x = winner(lst[:((len(lst)-1)//2)+1])
        y = winner(lst[((len(lst)-1)//2)+1:])
        # 반환된 값으로 가위바위보 연산
        return rcp(x, y)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 인덱스와 값을 함께 저장 [idx, i]의 형태
    lst = [[idx, i] for idx, i in enumerate(input().split(), 1)]
    print('#{} {}'.format(tc, winner(lst)[0]))
```

## 미로 -> range 설정 값 주의

```python
def find(r, c):
    # 전역변수인 flag를 사용
    global flag
    # delta 리스트를 돌아가며 0이 있는지 확인
    for i in range(4):
        r += dr[i]
        c += dc[i]
        # 0이 있다면 1로 만들고 다시 그 위치에서 find 함수 실행
        if arr[r][c] == 0:
            arr[r][c] = 1
            find(r, c)
        # 만약 3으로 이동할 수 있다면 flag = 1
        elif arr[r][c] == 3:
            flag = 1
            return
        # flag가 1이라면 다른 연산은 할 필요가 없으므로 return
        if flag == 1:
            return
        # 다시 r과 c 값을 초기화
        r -= dr[i]
        c -= dc[i]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # index error를 막기위해 4면을 모두 1로 채워 padding
    arr = [[1] + [int(i) for i in input()] + [1] for _ in range(N)]
    arr = [[1]*(N+2)] + arr + [[1]*(N+2)]
    # delta 값 리스트
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    # 3을 찾았다는 뜻의 flag
    flag = 0
    # 시작점인 2를 찾는다.
    for i in range(len(arr)):
        if 2 in arr[i]:
            r = i
            c = arr[i].index(2)
    # find 함수 실행
    find(r, c)
    print('#{} {}'.format(tc, flag))
```

## 배열 최소합 -> 백트래킹 조건 설정이 가장 중요

```python
def min_sum(lst):
    # 전역변수로 지정
    global min_val, sum_val
    # 길이가 N이라면 최솟값과 비교 후 최솟값을 구함
    if len(s) == N:
        min_val = min(min_val, sum_val)
        return
    # 리스트의 값이 스택에 있으면 continue
    for i in lst:
        if i in s:
            continue
    # 그렇지 않다면 스택에 추가하고 해당 위치의 값을 sum_val에 더함
        else:
            s.append(i)
            sum_val += arr[len(s)-1][i]
            # 만약 sum_val이 min_val보다 크다면 더이상 비교할 필요가 없으므로 초기화하고 continue
            if sum_val >= min_val:
                sum_val -= arr[len(s)-1][i]
                s.pop()
                continue
            # 크지 않다면 min_sum(lst)를 다시 한번 실행
            min_sum(lst)
            # 모두 실행한 이후 다시 초기화
            sum_val -= arr[len(s)-1][i]
            s.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최소값과 값들의 합을 정의
    min_val = 99999
    sum_val = 0
    # 스택
    s = []
    # 열의 범위가 0부터 N까지 임으로 0에서 N까지를 리스트로 만들어 함수에 대입
    min_sum(list(range(0, N)))
    print('#{} {}'.format(tc, min_val))

```

