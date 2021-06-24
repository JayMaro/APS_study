import heapq

T = int(input())
for _ in range(T):
    k = int(input())
    min_Q = []
    max_Q = []
    v = [0]*1000001
    for i in range(k):
        i_lst = input().split()
        if i_lst[0] == 'I':
            heapq.heappush(min_Q, (int(i_lst[1]), i))
            heapq.heappush(max_Q, (-int(i_lst[1]), i))
            v[i] = 1
        else:
            if i_lst[1] == '-1':
                while min_Q:
                    if v[min_Q[0][1]] == 0:
                        heapq.heappop(min_Q)
                    else:
                        x = heapq.heappop(min_Q)
                        v[x[1]] = 0
                        break

            else:
                while max_Q:
                    if v[max_Q[0][1]] == 0:
                        heapq.heappop(max_Q)
                    else:
                        y = heapq.heappop(max_Q)
                        v[y[1]] = 0
                        break

    while min_Q:
        if v[min_Q[0][1]] == 0:
            heapq.heappop(min_Q)
        else:
            break

    while max_Q:
        if v[max_Q[0][1]] == 0:
            heapq.heappop(max_Q)
        else:
            break

    if min_Q:
        print(-heapq.heappop(max_Q)[0], heapq.heappop(min_Q)[0])
    else:
        print('EMPTY')