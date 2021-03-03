

# SWEA

## D3

### 2805. 농작물 수확하기

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    n = 0
    res = 0
    while N//2 - n >= 0:
        for i in range(n, N-n):
            res += arr[N//2 + n][i]
            res += arr[N//2 - n][i]
            if n == 0:
                res -= arr[N//2][i]
        n += 1

    print('#{} {}'.format(t, res))

```



### Magnetic

```python
T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        s = []
        for j in range(N):
            if arr[j][i] != 0:
                s.append(arr[j][i])
        flag = 0
        for x in s:
            if flag != x:
                cnt += 1
                flag = x
        if s[0] == 2:
            cnt -= 1
        if s[-1] == 1:
            cnt -= 1

    print('#{} {}'.format(t, cnt//2))

```



### 거듭제곱

```python
def my_pow(N, M):
    if M == 0:
        return 1
    if M == 1:
        return N
    else:
        return N * my_pow(N, M-1)



T = 10
for t in range(1, T+1):
    testcase = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(testcase, my_pow(N, M)))
```



### 3456. 직사각형 길이 찾기

```python
T = int(input())
for tc in range(1, T+1):
    lst = map(int, input().split())
    s = []
    for i in lst:
        if i in s:
            s.remove(i)
        else:
            s.append(i)
    print('#{} {}'.format(tc, s.pop()))
```



### 3499. 퍼펙트 셔플

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = input().split()
    if len(lst) % 2:
        s1 = lst[:len(lst) // 2+1]
        s2 = lst[len(lst) // 2 +1:]
    else:
        s1 = lst[:len(lst)//2]
        s2 = lst[len(lst)//2:]
    res = []
    for i in range(len(s1)):
        res.append(s1[i])
        if i < len(s2):
            res.append(s2[i])
    print('#{}'.format(tc), end=' ')
    print(*res)
```



### ~~4698. 테네스의 특별한 소수~~

```python
아직 못품
```



### ~~5293. 이진 문자열 복원~~

```python
아직 못품
```





### ~~10965. 제곱수 만들기~~ -> 다시 풀어보기

```python
T = int(input())

prime = [2]
for i in range(3, int(10000000**(1/2)), 2):
    for p in prime:
        if i % p == 0:
            break
    else:
        prime.append(i)



for t in range(1, T + 1):
    N = int(input())
    result = 1
    if N**(1/2) == int(N**(1/2)):
        print(f'#{t} 1')
        continue

    for p in prime:
        if N < p:
            break
        cnt = 0
        while N % p == 0:
            cnt += 1
            N = N//p

        if cnt % 2:
            result *= p
        if N == 1:
            break
    if N > 1:
        result *= N

    print(f'#{t} {result}')
```

