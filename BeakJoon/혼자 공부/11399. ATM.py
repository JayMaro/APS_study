N = int(input())
lst = list(map(int, input().split()))
lst.sort()
now = 0
sum_val = 0
for num in lst:
    now += num
    sum_val += now
print(sum_val)