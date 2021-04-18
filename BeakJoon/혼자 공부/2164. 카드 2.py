from collections import deque

N = int(input())
lst = list(range(1, N+1))
lst = deque(lst)
while len(lst) != 1:
    lst.popleft()
    lst.append(lst.popleft())
print(lst[0])

