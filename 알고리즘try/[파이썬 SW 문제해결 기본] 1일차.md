# [파이썬 S/W 문제해결 기본] 1일차

## 4828. min max

```python
T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    case_num = int(input())
    case_lst = list(map(int, input().split()))
    # 최댓값과 최솟값을 선언
    max_value = 0
    min_value = 1000001
    # 각 case를 돌면서 최댓값과 최솟값을 찾음
    for i in case_lst:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
	# 최댓값과 최솟값의 차이를 저장
    diff = max_value - min_value
    print(f'#{t} {diff}')

  
```



## 4831. 전기버스 -> 좀 더 깔끔하게 코딩하도록 노력해보자

```python
T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    K, N, M = map(int, input().split())
    stop_lst = [0]*(N+1)
    stop_lst_num = list(map(int, input().split()))
    # 입력받은 리스트를 각 인덱스에 1로 저장
    for lst_num in stop_lst_num:
        stop_lst[lst_num] = 1
    # 전기 버스의 운행이 가능한가를 나타내는 변수 선언
    possible = True
    # i를 선언
    i = K
    # 충전횟수 선언
    cnt = 0
    while i < N+1:
        # 마지막 정류장이라면 break(while문 break)
        if i == N:
            break
        # 1씩 빼기위해 미리 1을 더해줌
        i += 1
        # 1씩 K번 빼면서 충전소 유무를 확인
        for x in range(K):
            i -= 1
            # 충전소가 잇다면 cnt를 1 증가시키고 계속 진행(for문 break)
            if stop_lst[i] == 1:
                cnt += 1
                break
		# 만약 반복문을 다 돌았다면 충전소가 없는 것이므로 possible = False 후 중지 (while문 break)
        else:
            possible = False
            break
		# i에 K를 더해서 다음 반복 진행
        i += K

	# possible이라면 cnt 출력 그렇지 않다면 0을 출력
    if possible:
        print(f'#{t} {cnt}')
    else:
        print(f'#{t} 0')


```

```python
T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    c_station = list(map(int, input().split()))

    # i = 0
    #
    # i + K 를 했을 때 만약 c_station의 다음 값이 i+K보다 작다면 다음값까지 넘어간다
    # i+ K 보다 작은 최대값을 찾은 후 cnt 1을 더한다
    # i + K보다 작은 다음 값이 없다면 정지한다
    # i의 값이 N이 된다면 끝낸다

    i = 0
    cnt = 0
    possible = True

    i += K
    for c in range(len(c_station)):
        if i >= c_station[c]:
            if c != len(c_station)-1:
                if i >= c_station[c+1]:
                    continue
            i = c_station[c]
            i += K
            cnt += 1
            if i >= N:
                break

        else:
            possible = False
            break


    if possible:
        print(f'#{t} {cnt}')
    else:
        print(f'#{t} 0')

```





## 4834. 숫자 카드

```python
T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    card_lst = [0]*10
    card_num = int(input())
    card = int(input())
    # 입력받은 숫자를 10으로 나눈 나머지들을 각각의 인덱스로 1씩 올리며 저장
    for i in range(card_num):
        card_lst[card % 10] += 1
        card = card // 10
	# 최댓값과 최댓값의 인덱스 값을 구함
    max_card = 0
    max_idx = 0
    for i in range(10):
        if card_lst[i] >= max_card:
            max_card = card_lst[i]
            max_idx = i

    print(f'#{t} {max_idx} {max_card}')
```



## 4835. 구간합 -> 좀 더 반복을 줄일 수 있는 방법을 생각해보자

```python
T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    N, M = map(int, input().split())
    i_lst = list(map(int, input().split()))
    # 최댓값 최솟값 선언
    min_val = 1000000000
    max_val = 0
    # range(0, N-M+1) -> 반복 횟수를 길이만큼 줄임
    for i in range(0, N-M+1):
        # 숫자들의 합을 선언하고 합하는 숫자의 갯수만큼 반복 덧셈
        lst_sum = 0
        for j in range(M):
            lst_sum += i_lst[i+j]
        # 최댓값과 최솟값 비교
        if lst_sum > max_val:
            max_val = lst_sum
        if lst_sum < min_val:
            min_val = lst_sum
    # 최댓값과 최솟값의 차이를 저장
    lst_diff = max_val - min_val

    print(f'#{t} {lst_diff}')

```



## 1945. 간단한 소인수분해

```python
T = int(input())

# 인수의 수를 구하는 함수
def check(num, div):
    cnt = 0
    while num % div == 0:
        cnt += 1
        num = num //div
        if num == 0:
            return cnt

    return cnt


for t in range(1, T+1):
    N = int(input())
    check_lst = [0]*5
    check_lst[4] = check(N, 11)
    check_lst[3] = check(N, 7)
    check_lst[2] = check(N, 5)
    check_lst[1] = check(N, 3)
    check_lst[0] = check(N, 2)

    print(f'#{t}', end=' ')
    for i in check_lst:
        print(i, end=' ')
    print()
   
```



## 5789. 현주의 상자 바꾸기

```python
T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())
    result = [0]*N
    # Q만큼 추가적으로 input을 받음 -> for문으로 작성
    # L과 R을 입력받고 range(L, R+1)만큼 반복하며 i를 저장
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            result[j-1] = i

    print(f'#{t}', end=' ')
    for res in result:
        print(res, end=' ')
    print()
```



