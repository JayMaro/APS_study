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



### 10200. 구독자 전쟁

```python
T = int(input())
for t in range(1, T+1):
    N, A, B = map(int, input().split())
    if A+B-N < 0:
        res = 0
    else:
        res = A+B-N
    print('#{} {} {}'.format(t, min(A, B), res))
```



### 9700. USB 꽂기의 미스터리

```python
T = int(input())
for t in range(1, T+1):
    p, q = map(float ,input().split())
    # s1 -> 처음에 반대로 잡고 뒤집에서 꽂았을 때 꽂힐 확률
    # s2 -> 처음에 제대로 잡고 꽂지 못해 2번 돌려서 꽂았을 때 꽂힐 확률
    s1 = (1-p) * q
    s2 = p*(1-q)*q
    if s1 < s2:
        print('#{} YES'.format(t))
    else:
        print('#{} NO'.format(t))
```



### 7675. 통역사 성경이

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    str1 = input().split()
    name_lst = []
    cnt = 0
    for word in str1:
        if word.title() == word and word.isalpha() is True:
            cnt += 1
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            if word[:-1].title() == word[:-1] and word[:-1].isalpha() is True:
                cnt += 1
            name_lst.append(cnt)
            cnt = 0

    print('#{}'.format(t), end=' ')
    for i in name_lst:
        print(i, end=' ')
    print()

```



### 6485. 삼성시의 버스 노선

```python
T = int(input())
 
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    bus = [0]*5001
    N = int(input())
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus[i] += 1
    P = int(input())
    for p in range(P):
        num = int(input())
        print(bus[num], end=' ')
 
    print()
```



### 6692. 다솔이의 월급 상자

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [input().split() for i in range(N)]
    res = 0
    for a in arr:
        p, x = float(a[0]), int(a[1])
        res += p*x
    print('#{} {}'.format(t, res))
```



### 6190. 정곤이의 단조 증가하는 수

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    max_val = -1
    for i in range(N):
        for j in range(i+1, N):
            tmp = num_lst[i]*num_lst[j]
            before = 9
            present = 0
            while tmp:
                present = tmp % 10
                if present <= before:
                    before = present
                    tmp //= 10
                    continue
                else:
                    break
            else:
                if num_lst[i]*num_lst[j] > max_val:
                    max_val = num_lst[i]*num_lst[j]
    print('#{} {}'.format(t, max_val))
```



### 6057. 그래프의 삼각형

```python
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_dict = {key: [] for key in range(1, N+1)}
    cnt = 0
    for i in range(M):
        x, y = map(int, input().split())
        num_dict[x].append(y)
        num_dict[y].append(x)

    for num, val in num_dict.items():
        for i in range(len(val)):
            for j in range(i+1, len(val)):
                if val[j] in num_dict[val[i]]:
                    cnt += 1
    cnt = cnt//3
    print('#{} {}'.format(t, cnt))

```

#### 참고하면 좋을 코드

```python
for t in range(int(input())):
  n,m=map(int,input().split())
  graph=[[0]*(n+1) for _ in range(n+1)]
  cnt=0
  for _ in range(m):
    x,y=map(int,input().split())
    graph[x][y]=1
    graph[y][x]=1
 
  for i in range(1,n+1):
    for j in range(i+1,n+1):
      for k in range(j+1,n+1):
        if graph[i][j]==1 and graph[j][k]==1 and graph[k][i]==1:
          cnt+=1
 
  print('#%d %d' %(t+1,cnt))
```



### 6019. 기차사이의 파리

```python
T = int(input())
for x in range(1, T+1):
  
    D, A, B, F = map(int, input().split())
    T = D/(A+B)
    flag = 'A'
    time = 0
    res = 0
    while time < T:
        if flag == 'A':
            t = D/(F+B)
            D = (F-A)*t
            res += F * t
            if t < 10e-8:
                break
            time += t
            flag = 'B'

        if flag == 'B':
            t = D/(F+A)
            D = (F-B)*t
            res += F * t
            if t < 10e-8:
                break
            time += t
            flag = 'A'


    print('#{} {}'.format(x, res))
```



### 5986. 새샘이와 세 소수

```python
prime = [2]
for i in range(3, 1000, 2):
    for p in prime:
        if i < p:
            continue
        if i % p == 0:
            break
    else:
        prime.append(i)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(len(prime)):
        if prime[i]> N:
            break
        for j in range(i, len(prime)):
            if prime[i] + prime[j] > N:
                break
            for k in range(j, len(prime)):
                if prime[i] + prime[j] + prime[k] > N:
                    break
                if prime[i] + prime[j] + prime[k] == N:

                    cnt += 1
    print('#{} {}'.format(t, cnt))
```



### 5948. 새샘이의 7-3-5 게임 -> 오랜만에 bubble sort

```python
T = int(input())
for t in range(1, T + 1):
    num_lst = list(map(int, input().split()))
    tmp = []
    for i in range(len(num_lst)):
        for j in range(i+1, len(num_lst)):
            for k in range(j+1, len(num_lst)):
                tmp.append(num_lst[i] + num_lst[j] + num_lst[k])

    res = list(set(tmp))

    for i in range(len(res)-1):
        for j in range(len(res)-1):
            if res[j+1] < res[j]:
                res[j], res[j+1] = res[j+1], res[j]

    print('#{} {}'.format(t, res[-5]))
```


