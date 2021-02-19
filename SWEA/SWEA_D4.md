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

