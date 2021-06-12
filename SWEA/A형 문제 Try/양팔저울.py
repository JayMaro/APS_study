def check(idx, left, right):
    if idx == N:
        memo.append(left - right)
    check(idx + 1, left + lst[idx], right)
    check(idx + 1, left, right + lst[idx])
    check(idx + 1, left, right)

N = int(input())
lst = list(map(int, input().split()))
memo = []