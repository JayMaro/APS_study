# [파이썬 S/W 문제해결 기본] 2일차

## 4836. 색칠하기

```python
T = int(input())

for t in range(1, T+1):
    N = int(input())
    red = [[0]*10 for _ in range(10)]
    blue = [[0]*10 for _ in range(10)]
    color = [0, red, blue]
    cnt = 0

    for _ in range(N):
        x1, y1, x2, y2, col = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                color[col][i][j] = col

    for i in range(10):
        for j in range(10):
            if red[i][j] and blue[i][j]:
                cnt += 1
    print(f'#{t} {cnt}')
```



## 4837. 부분집합의 합

```python
T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    res = 0
    for i in range(0, 1<<12):
        cnt = 0
        sum_val = 0

        for j in range(12):
            if i & (1<<j):
                cnt += 1
                sum_val += (j+1)
        if cnt == N and sum_val == K:
            res += 1

    print(f'#{t} {res}')
```



## 4839. 이진탐색

```python
T = int(input())

def div_page(page, purpose):
    l = 1
    r = page
    cnt = 0
    c = 1
    while c != purpose:
        c = int((l+r)/2)
        cnt += 1
        if c > purpose:
            r = c
        elif c < purpose:
            l = c
    return cnt

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_a = div_page(P, A)
    cnt_b = div_page(P, B)
    
    print(f'#{t} ', end='')
    if cnt_b == cnt_a:
        print(0)
    elif cnt_b < cnt_a:
        print('B')
    else:
        print('A')
```



## 4843. 특별한 정렬

```python
T = int(input())

for t in range(1, T+1):
    N = int(input())
    a_lst = [0]*101
    i_lst = list(map(int, input().split()))
    sorted_a_lst = []
    res = []
    for i in i_lst:
        a_lst[i] += 1

    for a in range(101):
        if a_lst[a] != 0:
            for _ in range(a_lst[a]):
                sorted_a_lst.append(a)

    print(f'#{t} ',end='')
    for i in range(5):
        print(sorted_a_lst[-i-1], end=' ')
        print(sorted_a_lst[i], end=' ')
    print()
```

