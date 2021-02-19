# 파이썬 SW문제해결 기본 - String



## 문자열 비교

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    if str2.find(str1) == -1:
        print('#{} 0'.format(t,))
    else:
        print('#{} 1'.format(t, ))
```



## 회문

```python
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for i in range(N)]
    # 가로줄 확인
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                print('#{}'.format(t), end=' ')
                print(''.join(arr[i][j:j+M]))

    # 가로 세로 바꿈
    for i in range(N):
        for j in range(i, N):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    # 바꾼 행렬 가로줄 확인
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                print('#{}'.format(t), end=' ')
                print(''.join(arr[i][j:j+M]))
```



## 글자수

```python
T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    char_dict = {}
    for char in str1:
        # 이미 key 값이 존재한다면 continue
        if char_dict.get(char, -1) != -1:
            continue
        # 그렇지 않다면 key값에 str2에서의 char의 갯수를 value로 지정
        char_dict[char] = str2.count(char)
    print('#{} {}'.format(t, max(char_dict.values())))
```

