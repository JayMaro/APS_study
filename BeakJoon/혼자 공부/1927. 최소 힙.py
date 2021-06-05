import heapq, sys
input = sys.stdin.readline
N = int(input().rstrip())
q = []
heapq.heapify(q)
for _ in range(N):
    x = int(input().rstrip())
    if x == 0:
        if q == []:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)