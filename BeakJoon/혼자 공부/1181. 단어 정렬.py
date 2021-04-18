N = int(input())
lst = [input() for _ in range(N)]
lst = list(set(lst))
lst.sort(key=lambda x: (len(x), x))
for ch in lst:
    print(ch)