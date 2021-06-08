import heapq, sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if q == []:
            print(0)
        else:
            res = heapq.heappop(q)
            print(res[1])
    else:
        heapq.heappush(q, (-x, x))