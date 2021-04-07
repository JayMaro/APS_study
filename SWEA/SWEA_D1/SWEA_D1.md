# SWEA

## D1



### 2072. 홀수만 더하기

```python
T = int(input())

for test_case in range(1, T + 1):
    
    list1 = []
    list_sum = 0
    list1 = map(int,input().split(' '))
    
    for i in list1:
        if i % 2 == 1:
            list_sum += i
            
    print("#{}".format(test_case), end = ' ')
    print(list_sum)
```



### 2071. 평균값 구하기

```python
import math

T = int(input())

for test_case in range(1, T + 1):
    
    list1 = []
    list_sum = 0
    list1 = list(map(int,input().split(' ')))
    
    for i in list1:
        list_sum += i
            
    print("#{}".format(test_case), end = ' ')
    list_avg = list_sum/len(list1)
    print(round(list_avg))
```



### 2070. 큰놈, 작은 놈, 같은 놈

```python
T = int(input())

for test_case in range(1, T + 1):
    list1 = []
    num1, num2 = map(int,input().split(' '))
    print("#{}".format(test_case), end = ' ')
    if num1 > num2:
        print('>')
    elif num1 == num2:
        print('=')
    else:
        print('<')
```



### 2068. 최대수 구하기

```python
import math

T = int(input())

for test_case in range(1, T + 1):
    
    list1 = []
    list_sum = 0
    list1 = list(map(int,input().split(' ')))
    
    
            
    print("#{}".format(test_case), end = ' ')
    print(max(list1))
```



### 2063. 중간 값 찾기

```python
N = int(input())
list1 = []
list1 = list(map(int,input().split(' ')))
list1.sort()

print(list1[int(N/2)])
```



### 2058. 자릿수 더하기

```python
def sum_of_digit(number):
    sum = 0
    while number:
        sum += number%10
        number = number // 10
        
    return sum

N = int(input())
print(sum_of_digit(N))
```



### 2056. 연월일 달력

```python
T = int(input())

for test_case in range(1, T + 1):
    
    month_31 = [1,3,5,7,8,10,12]
    month_30 = [4,6,9,11]

    input_str = input()
    year = input_str[:4]
    month = int(input_str[4:6])
    day = int(input_str[6:])
    
    if not 1<=month<=12:
        print("#{} -1".format(test_case))

        continue
    
    if month in month_31:
        if not 1<=day<=31:
            print("#{} -1".format(test_case))
            continue
    elif month in month_30:
        if not 1<=day<=30:
            print("#{} -1".format(test_case))
            continue
    elif month == 2:
        if not 1<=day<=28:
            print("#{} -1".format(test_case))
            continue


    print("#{}".format(test_case), end = ' ')
    print("{}/{:02}/{:02}".format(year,month,day))
```



### 2050. 알파벳을 숫자로 변환

```python
word = input()
for i in word:
    print(ord(i)-64, end = ' ')

```



### 2047. 신문 헤드라인

```python
word = input()
print(word.upper())
```



### 2046. 스탬프 찍기

```python
N = int(input())
for i in range(N):
    print('#', end = '')
```



### 2043. 서랍의 비밀번호

```python
P, K = map(int, input().split())
count = 1
while True:
    if K == P:
        print(count)
        break
    K += 1
    count += 1
```



### 2029. 몫과 나머지 출력하기

```python
T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int,input().split())
    print("#{}".format(test_case), end = ' ')
    print(a//b, a%b)
    
```



### 2027. 대각선 출력하기

```python
string_x = '+++++'

for idx in range(len(string_x)):
    string_y = []
    string_y += string_x
    string_y[idx] = '#'
    print(''.join(string_y))
```



### 2025. N줄덧셈

```python
N = int(input())
N_sum = 0
for i in range(1,N+1):
    N_sum += i
print(N_sum)
```



### 1938. 아주 간단한 계산기 

```python
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
```



### 1933. 간단한 N 의 약수

```python
N = int(input())
for i in range(1,N+1):
    if N % i == 0:
        print(i, end = ' ')
```



### 1936. 1대1 가위바위보 D1

```python
a, b = map(int,input().split())

if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')

elif a == 2:
    if b == 3:
        print('B')
    elif b == 1:
        print('A')

elif a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')

```



### 2019. 더블더블

```python
N = int(input())
for i in range(0,N+1):
    print(2**i, end = ' ')
```



### 1545. 거꾸로 출력해 보아요 D1

```python
N = int(input())
for i in range(N,-1,-1):
    print(i, end = ' ')
```

