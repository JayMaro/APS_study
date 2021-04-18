number = [0] * 1001
prime = []
for i in range(2, 40):
    if number[i] == 0:
        prime.append(i)
        n = 1
        while True:
            number[i*n] = 1
            n += 1
            if i*n > 1000:
                break
for i in range(40, 1001):
    if number[i] == 0:
        prime.append(i)

N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for num in lst:
    if num in prime:
        cnt += 1
print(cnt)

