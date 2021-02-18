# SWEA

## D3



###  11387. 몬스터 사냥

```python
T = int(input())

for t in range(1, T+1):
    D, L, N = map(int, input().split())
    damage = 0
    for n in range(N):
        damage += D*(1+n*(L/100))
    print(f'#{t} {int(damage)}')
```



### 11315. 오목 판정

```python
T = int(input())
 
for t in range(1, T+1):
    N = int(input())
    om_arr = []
    res = False
    for i in range(N):
        i_lst = []
        data = input()
        for om in data:
            i_lst.append(om)
        om_arr.append(i_lst)
 
    # 행
    for i in range(N):
        cnt = 0
        for j in range(N):
            if om_arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    res = True
            else:
                cnt = 0
    # 열
    for i in range(N):
        cnt = 0
        for j in range(N):
            if om_arr[j][i] == 'o':
                cnt += 1
                if cnt >= 5:
                    res = True
            else:
                cnt = 0
    # 오른쪽 아래
    for i in range(N):
        for j in range(N):
            cnt = 0
            x, y = i, j
            while om_arr[x][y] == 'o':
                cnt += 1
                x += 1
                y += 1
                if cnt >= 5:
                    res = True
 
                if x == N or y == N:
                    break
                     
 
    # 왼쪽 아래
    for i in range(N):
        for j in range(N-1, -1, -1):
            cnt, y, x = 0, j, i
            while om_arr[x][y] == 'o':
                cnt += 1
                y -= 1
                x += 1
                if cnt >= 5:
                    res = True
                if y < 0 or x == N:
                    break
    if res:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')

```

###  10570. 제곱 팰린드롬 수  -> 제곱근 확인 하는 법 알아보기

```python
T = int(input())
# 팰린드롬 함수를 정의
# 제곱과 제곱근에 각각 함수를 적용 둘다 True면 cnt 추가
def palin(num):
    num_lst = []
    while num:
        num_lst.append(num%10)
        num = num//10
    while True:
        if len(num_lst) <= 1:
            return True
        if num_lst[0] == num_lst[-1]:
            num_lst = num_lst[1:-1]
            continue
        else:
            return False



for t in range(1, T+1):
    cnt = 0
    A, B = map(int, input().split())
    for i in range(A, B+1):
        if not int(i**(1/2))**2 == i:
            continue
        if palin(i) and palin(i**(1/2)):
            cnt += 1
    print(f'#{t} {cnt}')
```



### 10505. 소득 불균형

```python
T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    num_sum = 0
    for i in num_lst:
        num_sum += i
    num_avg = num_sum / N
    cnt = 0
    for j in num_lst:
        if j <= num_avg:
           cnt += 1
    print(f'#{t} {cnt}')
```



### 11315. 오목 판정

```python
T = int(input())

for t in range(1, T+1):
    N = int(input())
    om_arr = []
    res = False
    for i in range(N):
        i_lst = []
        data = input()
        for om in data:
            i_lst.append(om)
        om_arr.append(i_lst)

    # 행
    for i in range(N):
        cnt = 0
        for j in range(N):
            if om_arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    res = True
            else:
                cnt = 0
    # 열
    for i in range(N):
        cnt = 0
        for j in range(N):
            if om_arr[j][i] == 'o':
                cnt += 1
                if cnt >= 5:
                    res = True
            else:
                cnt = 0
    # 오른쪽 아래
    for i in range(N):
        for j in range(N):
            cnt = 0
            x, y = i, j
            while om_arr[x][y] == 'o':
                cnt += 1
                x += 1
                y += 1
                if cnt >= 5:
                    res = True

                if x == N or y == N:
                    break


    # 왼쪽 아래
    for i in range(N):
        for j in range(N-1, -1, -1):
            cnt, y, x = 0, j, i
            while om_arr[x][y] == 'o':
                cnt += 1
                y -= 1
                x += 1
                if cnt >= 5:
                    res = True
                if y < 0 or x == N:
                    break
    if res:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')
```



### 다트게임

```python
T = int(input())


def point(distance):
    point_lst = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    for p in range(len(point_lst)):
        if distance <= point_lst[p]:
            return 10 - p
    return 0


for t in range(1, T + 1):
    N = int(input())
    i_sum = 0
    for i in range(N):
        x, y = map(int, input().split())
        dis = (x ** 2 + y ** 2) ** (1 / 2)
        i_sum += point(dis)
    print(f'#{t} {i_sum}')
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



### 10912. 외로운 문자

```python
T = int(input())

for t in range(1, T + 1):
    word = input()
    leave = []
    for char in word:
        if char in leave:
            leave.remove(char)
        else:
            leave.append(char)

    leave.sort()
    if leave == []:
        print(f'#{t} Good')
    else:
        print(f'#{t}', end=' ')
        for i in leave:
            print(i, end='')
        print()
```



### 10804. 문자열의 거울상

```python
T = int(input())

for t in range(1, T + 1):
    word = input()
    res = ''
    bdpq_dict = {
        'b': 'd',
        'd': 'b',
        'p': 'q',
        'q': 'p',
    }
    for char in word:
        res = bdpq_dict[char] + res

    print(f'#{t} {res}')
```



### 10761. 신뢰 -> 더 쉽게 풀 수 있는데 너무 어렵게 풀었다...

```python
T = int(input())


def time_cal(location, purpose):
    return abs(purpose - location) + 1


for t in range(1, T + 1):
    i_lst = input().split()
    N = i_lst[0]
    turn, B_lst, O_lst = [], [], []
    present, before_b,before_o, x, y = 0, 0, 0, 0, 0
    location_b, location_o = 1, 1

    for i in range(1, len(i_lst), 2):
        turn.append(i_lst[i])
        if i_lst[i] == 'B':
            B_lst.append(i_lst[i + 1])
        else:
            O_lst.append(i_lst[i + 1])

    for i in turn:
        if i == 'B':
            purpose_b = int(B_lst[x])
            x += 1

            if before_b + time_cal(location_b, purpose_b) <= present:
                present += 1
            else:
                present = before_b + time_cal(location_b, purpose_b)

            location_b = purpose_b
            before_b = present

        if i == 'O':
            purpose_o = int(O_lst[y])
            y += 1
            if before_o + time_cal(location_o, purpose_o) <= present:
                present += 1
            else:
                present = before_o + time_cal(location_o, purpose_o)

            location_o = purpose_o
            before_o = present

    print(f'#{t} {present}')
```



### 10726. 이진수 표현

```python
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    binary_num = str(bin(M))[2:]
    flag = True
    if len(binary_num) >= N:
        for num in range(-1, -N-1, -1):
            if binary_num[num] != '1':
                flag = False
    else:
        flag = False

    if flag:
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')
```



### 10580. 전봇대

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                cnt += 1
    print('#{} {}'.format(t, cnt))
```

