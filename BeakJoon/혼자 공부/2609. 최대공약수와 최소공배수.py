N, M = map(int, input().split())
num1, num2 = N, M
i = 2
N_measure = []
M_measure = []
while N != 1:
    if N % i == 0:
        N_measure.append(i)
        N //= i
        i = 2
        continue
    i += 1

while M != 1:
    if M % i == 0:
        M_measure.append(i)
        M //= i
        i = 2
        continue
    i += 1

measure = 1
for num in N_measure:
    if num in M_measure:
        measure *= num
        M_measure.remove(num)

res = (num1//measure) * (num2//measure) * measure
print(measure)
print(res)