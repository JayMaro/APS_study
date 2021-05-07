# 분할정복의 중요성
# 점화식을 만들어서 풀자

def div_con(num, i):
    if i == 1:
        return num % C
    if i % 2:
        return (div_con(num, i // 2) ** 2 * A) % C

    else:
        return (div_con(num, i // 2) ** 2) % C


A, B, C = map(int, input().split())
print(div_con(A, B))
