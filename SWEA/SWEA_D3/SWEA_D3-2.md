# SWEA

## D3



### 5688. 세제곱근을 찾아라

```python
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    r_N = round(N**(1/3))
    if r_N**3 == N:
        print('#{} {}'.format(t, r_N))
    else:
        print('#{} -1'.format(t))
```



### 5549. 홀수일까 짝수일까

```python
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    if N % 2:
        print('#{} {}'.format(t, 'Odd'))
    else:
        print('#{} {}'.format(t, 'Even'))
```



### 5515. 2016년 요일 맞추기 -> 인덱스인지 요소인지 잘 확인하자

```python
T = int(input())
for t in range(1, T + 1):
    m, d = map(int, input().split())
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = -1
    for i in range(m):
        day += month[i]
    day += d+4
    res = day % 7
    print('#{} {}'.format(t, res))
```



### 5431. 민석이의 과제 체크하기

```python
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    sub_lst = list(map(int, input().split()))
    p_lst = [i for i in range(1, N+1)]
    for num in sub_lst:
        p_lst.remove(num)
    print('#{}'.format(t), end=' ')
    for i in p_lst:
        print(i, end=' ')
    print()
```



###  5356. 의석이의 세로로 말해요

```python
T = int(input())
for t in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    res = ''
    max_len = 0
    # 행 길이의 최대 길이 구하기
    for lst in arr:
        if len(lst) > max_len:
            max_len = len(lst)

    # 행 길이가 부족한 행에 -1을 추가하여 길이를 같게 만듦
    for lst in arr:
        while len(lst) < max_len:
            lst.append(-1)

    # -1이 나오면 넘어가고 아니라면 더해서 문자열을 완성
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] == -1:
                continue
            res += arr[j][i]

    print('#{} {}'.format(t, res))
```



### 4751. 다솔이의 다이아몬드 장식 

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    arr =['','','','','']
    i = 0
    for j in range(0, 4 * len(str1), 4):
        arr[0] += '..#.'
        arr[1] += '.#.#'
        arr[2] += '#.{}.'.format(str1[i])
        i += 1
        arr[3] += '.#.#'
        arr[4] += '..#.'

    arr[0] += '.'
    arr[1] += '.'
    arr[2] += '#'
    arr[3] += '.'
    arr[4] += '.'
    for y in arr:
        print(y)
```



### 5215. 햄버거 다이어트 -> 부분집합으로 풀었지만 DFS를 이용하는 방식을 보니 역시 고급 알고리즘을 써야겠따.

```python
T = int(input())
for t in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_taste = -1
    for i in range(1<<N):
        cal_sum, taste_sum = 0, 0
        for j in range(N):
            if i & (1<<j):
                cal_sum += arr[j][1]
                taste_sum += arr[j][0]
                if cal_sum > L:
                    break
                else:
                    if taste_sum > max_taste:
                        max_taste = taste_sum

    print('#{} {}'.format(t, max_taste))
```

```python
def dfs(idx, cal, score):
    global max_score
    if idx == N:
        max_score = max(max_score, score)
        return
    dfs(idx+1, cal, score)
    cal += lst[idx][1]
    if cal > L:
        return
    score += lst[idx][0]
    dfs(idx+1, cal, score)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, max_score))
```





### 5162. 두가지 빵의 딜레마

```python
T = int(input())
for t in range(1, T+1):
    # 둘 중 낮은 가격으로 총 가격을 나눈 갯수가 가장 적을 수 밖에 없다.
    A, B, C = map(int, input().split())
    res = C // min(A, B)

    print('#{} {}'.format(t, res))
```



### 4789. 성공적인 공연 기획

```python
T = int(input())
for t in range(1, T+1):
    lst = input()
    clap, hire = 0, 0
    for i in range(len(lst)):
        if clap >= i:
            clap += int(lst[i])
        else:
            while clap < i:
                hire += 1
                clap += 1
            clap += int(lst[i])
    print('#{} {}'.format(t, hire))
```



### 4676. 늘어지는 소리 만들기

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    H = int(input())
    lst = list(map(int, input().split()))
    cnt = [0] * (len(str1)+1)
    res = ''
    for i in lst:
        cnt[i] += 1
    if cnt[0] != 0:
        res += '-'*cnt[0]

    for j in range(1, len(cnt)):
        res += str1[j-1] + '-'*cnt[j]
        
    print('#{} {}'.format(t, res))
```



### 4522. 세상의 모든 팰린드롬

```python
def new_palin(strx):
    if len(strx) <= 1:
        return True
    if strx[0] == strx[-1] or strx[0] == '?' or strx[-1] == '?':
        return new_palin(strx[1:-1])
    else:
        return False


T = int(input())
for t in range(1, T+1):
    str1 = input()
    check = new_palin(str1)
    if check:
        print('#{} Exist'.format(t))
    else:
        print('#{} Not exist'.format(t))
```



### 4579. 세상의 모든 팰린드롬 2

```python
def new_palin(strx):
    if len(strx) <= 1:
        return True
    if strx[0] == strx[-1]:
        return new_palin(strx[1:-1])
    if strx[0] == '*':
        return True
    if strx[-1] == '*':
        return True
    else:
        return False


T = int(input())
for t in range(1, T+1):
    str1 = input()
    check = new_palin(str1)

    if check:
        print('#{} Exist'.format(t))
    else:
        print('#{} Not exist'.format(t))
```



### 4466. 최대 성적표 만들기

```python
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    score = 0
    for i in range(K):
        score += lst[i]
    print('#{} {}'.format(t, score))
```



### 4406. 모음이 보이지 않는 사람

```python
T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str1 = str1.replace('a','')
    str1 = str1.replace('e', '')
    str1 = str1.replace('i', '')
    str1 = str1.replace('o', '')
    str1 = str1.replace('u', '')
    print('#{} {}'.format(test_case, str1))
```



### 4299. 태혁이의 사랑은 타이밍

```python
T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    D, H, M = lst[0], lst[1], lst[2]
    diff_D = D - 11
    diff_H = H - 11
    diff_M = M - 11
    total = diff_D * 1440 + diff_H * 60 + diff_M
    if total < 0:
        total = -1
    print('#{} {}'.format(t, total))
```



### 4047. 영준이의 카드 카운팅

```python
T = int(input())
for t in range(1, T+1):
    lst = input()
    card = {'S': [],
            'D': [],
            'H': [],
            'C': [],}
    card_num = [13, 13, 13, 13]
    flag = True
    for i in range(0, len(lst), 3):
        if (''.join(lst[i+1:i+3])) in card[lst[i]]:
            flag = False
            continue
        card[lst[i]].append(''.join(lst[i+1:i+3]))

    card_num[0] -= len(card['S'])
    card_num[1] -= len(card['D'])
    card_num[2] -= len(card['H'])
    card_num[3] -= len(card['C'])


    if flag:
        print('#{} '.format(t), end='')
        for num in card_num:
            print(num, end=' ')
        print()
    else:
        print('#{} ERROR'.format(t))
```



### 3975. 승률 비교하기 -> 출력시 모아서 출력하는 것이 더 빠르다

```python
T = int(input())
res = []
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    alice = lst[0]/lst[1]
    bob = lst[2]/lst[3]
    if abs(alice - bob) < 10e-10:
        res.append('DRAW')
    elif alice > bob:
        res.append('ALICE')
    else:
        res.append('BOB')

for i in range(len(res)):
    print('#{} {}'.format(i+1, res[i]))
```



### 3431. 준환이의 운동관리

```python
T = int(input())
for t in range(1, T+1):
    L, U, X = map(int, input().split())
    print('#{} '.format(t), end='')
    if L - X > 0:
        print(L-X)
    elif U - X < 0:
        print('-1')
    else:
        print('0')
```



### 1289. 원재의 메모리 복구하기

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    cur = '0'
    cnt = 0
    for char in str1:
        if char == '1' and cur == '0':
            cnt += 1
            cur = '1'
        elif char == '0' and cur == '1':
            cnt += 1
            cur = '0'
    print('#{} {}'.format(t, cnt))
```



### 1860. 진기의 최고급 붕어빵

```python
T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    N, M, K = lst[0], lst[1], lst[2]
    people = list(map(int, input().split()))
    people.sort()
    flag = True
    for i in range(len(people)):
        if (people[i]//M)*K < i+1:
            flag = False
            break
    print('#{}'.format(t), end=' ')
    if flag:
        print('Possible')
    else:
        print('Impossible')
```



### 오셀로 승리했다!

```python
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    arr[N//2][N//2] = arr[N//2-1][N//2-1] = 2
    arr[N//2-1][N//2] = arr[N//2][N//2-1] = 1

    for m in range(M):
        x, y, stone = map(int, input().split())
        y = y-1
        x = x-1
        arr[y][x] = stone
        # 오른쪽
        for i in range(x+1, N):
            if arr[y][i] == 0:
                break
            elif arr[y][i] == stone:
                for j in range(x+1, i):
                    arr[y][j] = stone
                break
        # 왼쪽
        for i in range(x-1, -1, -1):
            if arr[y][i] == 0:
                break
            elif arr[y][i] == stone:
                for j in range(x-1, i, -1):
                    arr[y][j] = stone
                break
        # 아래
        for i in range(y+1, N):
            if arr[i][x] == 0:
                break
            elif arr[i][x] == stone:
                for j in range(y+1, i):
                    arr[j][x] = stone
                break
        # 위
        for i in range(y-1, -1, -1):
            if arr[i][x] == 0:
                break
            elif arr[i][x] == stone:
                for j in range(y-1, i, -1):
                    arr[j][x] = stone
                break
        # 오른쪽 위
        for i in range(1, N):
            if x+i < N and y-i > -1:
                if arr[y - i][x + i] == 0:
                    break
                elif arr[y-i][x+i] == stone:
                    for j in range(1, i):
                        arr[y-j][x+j] = stone
                    break
            else:
                break
        # 오른쪽 아래
        for i in range(1, N):
            if x+i < N and y+i < N:
                if arr[y + i][x + i] == 0:
                    break
                elif arr[y+i][x+i] == stone:
                    for j in range(1, i):
                        arr[y+j][x+j] = stone
                    break
            else:
                break
        # 왼쪽 위
        for i in range(1, N):
            if x-i > -1 and y-i > -1:
                if arr[y - i][x - i] == 0:
                    break
                elif arr[y-i][x-i] == stone:
                    for j in range(1, i):
                        arr[y-j][x-j] = stone
                    break
            else:
                break

        # 왼쪽 아래
        for i in range(1, N):
            if x-i > -1 and y+i < N:
                if arr[y + i][x - i] == 0:
                    break
                elif arr[y+i][x-i] == stone:
                    for j in range(1, i):
                        arr[y+j][x-j] = stone
                    break
            else:
                break

        # print('*'*20)
        # for i in arr:
        #     print(i)

    cnt_w = 0
    cnt_b = 0
    for i in arr:
        for j in i:
            if j == 1:
                cnt_b += 1
            elif j == 2:
                cnt_w += 1
    print('#{} {} {}'.format(t, cnt_b, cnt_w))
```




