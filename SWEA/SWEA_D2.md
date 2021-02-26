# SWEA

## D2

### ~~1859. 백만 장자 프로젝트~~

```python
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    
    c_list = list(map(int, input().split()))
    benefit = 0
    max = c_list[-1]
    for idx in range(N-1,-1,-1):
        if c_list[idx] >= max:
            max = c_list[idx]
        else:
            benefit += (max - c_list[idx])
    print("#{}".format(test_case), end = ' ')
    print(benefit)
```



### 1926. 간단한 369게임

```python
N = int(input())
for i in range(1,N+1):
    num = i
    clap = False
    while num:
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            print('-', end = '')
            clap = True
        num = num // 10
    
    if clap == False:
        print(i, end = ' ')
    else:
        print('', end = ' ')

```



### 2007. 패턴 마디의 길이

```python
T = int(input())
for i in range(1,T+1):
    

    input_string = input()
    first = input_string[0]
    for idx in range(1,30):
        if input_string[idx] == first:
            if input_string[:idx] == input_string[idx:idx*2]:
                print('#{} '.format(i), end = '')
                print(idx)
                break
        if idx == 29:
            print('#{} '.format(i), end = '')
            print(30)
    
```



### 2005. 파스칼의 삼각형

```python
# index 0과 -1은 1 고정
# index n의 값은 n-1과 n의 합
# 다만들고 total list에 추가
T = int(input())
for t in range(1,T+1):
    N = int(input())
    final_list = []
    for n in range(1, N+1):
        i_list = []
        for x in range(n):
            
            if x == 0:
                i_list.append(1)
            elif x == n-1:
                i_list.append(1)
            else:
                num = final_list[-1][x] + final_list[-1][x-1]
                i_list.append(num)

        final_list.append(i_list)
    
    print('#{}'.format(t))
    for final in final_list:
        for i in final:
            print(i, end = ' ')
        print()
    
```

### 재귀로 풀었지만 runtime error...

```python
res = [[0]]
def pascal(N):
    if N == 1:
        res.append([0, 1, 0])
        return
    else:
        pascal(N-1)
        triangle = []
        for i in range(N+2):
            if i == 0 or i == N+1:
                triangle.append(0)
            else:
                triangle.append(res[N-1][i-1] + res[N-1][i])
        res.append(triangle)
        return



T = int(input())
for t in range(1, T+1):
    N = int(input())
    pascal(N)
    print('#{}'.format(t))
    for x in res:
        if len(x) == 1:
            continue
        for y in range(1, len(x)-1):
            print(x[y], end=' ')
        print()

```





### 2001. 파리 퇴치

```python
# 리스트를 이용해 행과 열을 입력받음
# n*n 행렬에서 m*m행렬씩 움직임
# index는 0부터 -m까지
# 시작지점에서
# 열+1이 되면 행렬[][+1]씩
# 행+1이 되면 행렬[+1][]
# if 행렬[][] is 행렬 [-m][] or 행렬[][-m] 끝
# 0 1 2 3 4    5 - 3 2 
T = int(input())

for t in range(1,T+1):

    array = []
    array_N, array_M = map(int, input().split()) 

    for i in range(array_N):
        input_list = list(map(int, input().split()))
        array.append(input_list)

    max_sum = 0

    # 시작점 순환
    for idx_row in range(array_N-array_M+1):
        for idx_col in range(array_N-array_M+1):
            # 값 찾기
            array_sum = 0
            for i in range(array_M):
                for j in range(array_M):
                    array_sum += array[idx_row+i][idx_col+j]
            if array_sum > max_sum:
                max_sum = array_sum

    print(f'#{t} {max_sum}')

# 이중에 이중이라니... 이게 맞는 풀이일까?
```



### 1989. 초심자의 회문 검사

```python
# 회문 판별

T = int(input())
for t in range(1, T+1):
    
    decide = True
    input_string = input()
    while len(input_string) > 1:
        if input_string[0] == input_string[-1]:
            input_string = input_string[1:-1]
            
        else:
            print(f'#{t} 0')
            decide = False
            break
    if decide:
        print(f'#{t} 1')
```



### 1986. 지그재그 숫자

```python
T = int(input())
for t in range(1, T+1):
    
    N = int(input())
    int_sum = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            i = -i
        int_sum += i

    print(f'#{t} {int_sum}')
```



### 1984. 중간 평균값 구하기

```python
T = int(input())
for t in range(1,T+1):
    input_list = list(map(int,input().split()))
    input_list.remove(max(input_list))
    input_list.remove(min(input_list))
    
    input_sum = 0
    for i in input_list:
        input_sum += i
    
    input_avg = round(input_sum / len(input_list))

    print(f'#{t} {input_avg}')
```



### 1983. 조교의 성적 매기기

```python
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    cal_list = []
    for x in range(N):
        ilist = list(map(int, input().split()))
        cal_list.append(ilist[0]*0.35 + ilist[1]*0.45 + ilist[2]*0.2)
    
    result = [(i,idx) for idx, i in enumerate(cal_list)]
    sorted_result = sorted(result, key = lambda x: x[0])
    sorted_result.reverse()

    for index, i in enumerate(sorted_result):
        if i[1] == K-1:
            purpose = index
    
    print(f'#{t} ', end = '')

    if purpose < N//10:
        print('A+')
    elif purpose < N//10*2:
        print('A0')
    elif purpose < N//10*3:
        print('A-')
    elif purpose < N//10*4:
        print('B+')
    elif purpose < N//10*5:
        print('B0')
    elif purpose < N//10*6:
        print('B-')
    elif purpose < N//10*7:
        print('C+')
    elif purpose < N//10*8:
        print('C0')
    elif purpose < N//10*9:
        print('C-')
    else:
        print('D0')
```



### 1973. 어디에 단어가 들어갈 수 있을까

```python
T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    iarray = [list(map(int, input())) for i in range(N)]
    result = 0
    
    for i in range(N):
        cnt_r = 0
        cnt_c = 0
        for j in range(N):
            if iarray[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    result += 1
                cnt_r = 0

            if iarray[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    result += 1
                cnt_c = 0
        if cnt_r == K:
            result += 1
        if cnt_c == K:
            result += 1
            
            
    
    print(f'#{t} {result}')

```



### 1976. 시각 덧셈

```python
T = int(input())
for t in range(1,T+1):
    ilist = list(map(int, input().split()))
    t1 = ilist[:2]
    t2 = ilist[2:]

    minutes = t1[1] + t2[1]
    hours = t1[0] + t2[0]

    over = minutes // 60
    minutes %= 60
    
    if over:
        hours += 1
    
    hours %= 12
    if hours == 0:
        hours = 12

    print(f'#{t} {hours} {minutes}')
```



### 1974. 스도쿠 검증

```python
def check_square(iarray, idx):
    check_list_square = [0 for i in range(9)]
    for i in range(idx[0], idx[0]+3):
        for j in range(idx[0], idx[0]+3):
            check_list_square[iarray[i][j]-1] += 1
    if 0 in check_list_square:
        return 0
    
    return 1



T = int(input())
for t in range(1,T+1):
    iarray = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        check_list_r = [0 for i in range(9)]
        check_list_c = [0 for i in range(9)]
        for j in range(9):
            check_list_r[iarray[i][j]-1] += 1
            check_list_c[iarray[j][i]-1] += 1
        
        if 0 in check_list_r or 0 in check_list_c:
            result = 0
            break

    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not check_square(iarray, (i,j)):
                result = 0



    print(f'#{t} {result}')
```



### 1970. 쉬운 거스름돈

```python
T = int(input())
for t in range(1,T+1):
    money_list = []
    money = int(input())
    money_list.append(money//50000)
    money %= 50000
    money_list.append(money//10000)
    money %= 10000
    money_list.append(money//5000)
    money %= 5000
    money_list.append(money//1000)
    money %= 1000
    money_list.append(money//500)
    money %= 500
    money_list.append(money//100)
    money %= 100
    money_list.append(money//50)
    money %= 50   
    money_list.append(money//10)
    money %= 10 



    print(f'#{t}')
    for i in money_list:
        print(i, end=' ')
    print()
# 직관성은 좋지만 뭔가 지저분한 느낌...
```



### 1966. 숫자를 정렬하자

```python
T = int(input())
for t in range(1, T+1):
    N = int(input())
    i_list = list(map(int, input().split()))
    

    i_list.sort()
    print(f'#{t} ', end='')
    for i in i_list:
        print(i, end=' ')
    print()
```



### 1961. 숫자 배열

```python
T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
    N = int(input())
    n_lst = list()
    for n in range(N):
        n_lst.append(input().split())
    
    for i in range(N):
        for j in range(N):
            print(n_lst[-j-1][i], end='')
        print(end=' ')
        for j in range(N):
            print(n_lst[-i-1][-j-1], end='')
        print(end=' ')
        for j in range(N):
            print(n_lst[j][-i-1], end='')
        print()
# rotate 함수를 만들어서 계속 넣는 방법도 있었다.
# 완전 신선했다.
```



### 1959. 두 개의 숫자열

```python
# N과 M만큼 받는다.
# 두 배열의 길이를 확인한다.
# 배열의 길이가 긴 배열에서 작은 배열의 길이를 뺀 뒤 1을 더한 만큼 반복한다.
# 배열의 길이가 긴 배열을 작은 배열의 길이만큼 반복하며 계산한다.
# 길이가 긴 배열에 1씩 추가하며 계속 계산한다.
T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    max_value = -99999
    
    if N > M:
        long_lst = n_lst
        short_lst = m_lst
    else:
        long_lst = m_lst
        short_lst = n_lst


    for idx in range(len(long_lst) - len(short_lst) +1):
        sum_lst = 0
        for i in range(len(short_lst)):
            sum_lst += long_lst[i+idx] * short_lst[i]
        if sum_lst > max_value:
            max_value = sum_lst

    print(max_value)
```



### 1954. 달팽이 숫자

```python
T = int(input())

for t in range(1, T+1):
    N = int(input())
    snail = [[0]*N for i in range(N)]
    xy_lst = [[0,1], [1,0], [0,-1], [-1,0]]
    x = 0
    y = 0
    xy = 0
    for i in range(1, N**2+1):
        if snail[x][y] == 0:
            snail[x][y] = i

            x += xy_lst[xy%4][0]
            y += xy_lst[xy%4][1]

            if x == N or y == N or x == -1 or y == -1:
                x -= xy_lst[xy % 4][0]
                y -= xy_lst[xy % 4][1]
                xy += 1
                x += xy_lst[xy % 4][0]
                y += xy_lst[xy % 4][1]

        else:
            x -= xy_lst[xy % 4][0]
            y -= xy_lst[xy % 4][1]
            xy += 1
            x += xy_lst[xy % 4][0]
            y += xy_lst[xy % 4][1]
            snail[x][y] = i
            x += xy_lst[xy % 4][0]
            y += xy_lst[xy % 4][1]

    print(f'#{t}')
    for i in snail:
        for j in i:
            print(j, end=' ')
        print()
```



### 1948. 날짜 계산기

```python

T = int(input())

month = {'1': 31,
         '2': 28,
         '3': 31,
         '4': 30,
         '5': 31,
         '6': 30,
         '7': 31,
         '8': 31,
         '9': 30,
         '10': 31,
         '11': 30,
         '12': 31,
         }

for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    sum_day = 0
    for i in range(m1, m2):
        sum_day += month[f'{i}']
    if m1 == m2:
        sum_day *= 2
    sum_day = sum_day - d1 + d2 + 1
    print(f'#{t} {sum_day}')

```



### 1946. 간단한 압축 풀기

```python
T = int(input())


for t in range(1, T+1):
    print(f'#{t}')
    N = int(input())
    char_lst = []
    for i in range(N):
        C, K = input().split()
        char_lst.append([C, int(K)])
    str_o = ''
    for char in char_lst:
        while char[1] != 0:
            if len(str_o) == 10:
                print(str_o)
                str_o = ''
            str_o += char[0]
            char[1] -= 1

    print(str_o)
```



### 1940. 가랏! RC카!

```python
T = int(input())


for t in range(1, T+1):
    V = 0
    distance = 0
    N = int(input())
    for n in range(N):
        time_lst = list(map(int, input().split()))
        if time_lst[0] == 0:
            distance += V
        elif time_lst[0] == 1:
            V += time_lst[1]
            distance += V
        elif time_lst[0] == 2:
            V -= time_lst[1]
            if V < 0:
                V = 0
            distance += V
    print(f'#{t} {distance}')
```



### 1928. Base64 Decoder

```python
import base64
T = int(input())

for t in range(1, T+1):
    i_str = input()
    o_str = str(base64.b64decode(i_str))
    print(f'#{t} {o_str[2:-1]}')

```



### 1288. 새로운 불면증 치료법

```python
T = int(input())

for t in range(1, T+1):
    # 숫자를 입력 받는다 : N
    # N에 숫자를 곱해가며 각 자리수를 저장한다
    # 리스트를 만들어 각 자릿수가 나온 여부를 저장한다.
    # 곱셈으로 0이 아니면 끝
    N = int(input())
    c_lst = [0]*10
    i = 0
    while c_lst[0]*c_lst[1]*c_lst[2]*c_lst[3]*c_lst[4]*c_lst[5]*c_lst[6]*c_lst[7]*c_lst[8]*c_lst[9] == 0:
        i += 1
        tmp = N*i
        while tmp:
            c_lst[tmp%10] += 1
            tmp = tmp//10
    print(f'#{t} {N*i}')
```



### 1284. 수도 요금 경쟁

```python
T = int(input())

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    # P*W => 그냥 요금
    # W가 R 초과 Q + S
    # W가 R 이하 Q
    A = P*W

    if W > R:
        B = Q + S*(W-R)
    else:
        B = Q

    print(f'#{t}', end=' ')
    if A<B:
        print(A)
    else:
        print(B)
```



### 1204. 최빈수 구하기

```python
T = int(input())

for t in range(1, T+1):
    num = int(input())
    s_lst = [0]*101
    score = list(map(int, input().split()))
    for i in score:
        s_lst[i] += 1
    max_value = 0
    max_idx = 0
    for s in range(len(s_lst)):
        if s_lst[s] >= max_value:
            max_value = s_lst[s]
            max_idx = s
    print(f'#{num} {max_idx}')
```

