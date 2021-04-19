def dfs(i):
    global score, cal_sum, max_score
    visited[i] = 1
    s.append(lst[i])
    score += lst[i][0]
    cal_sum += lst[i][1]
    if cal_sum > L:
        max_score = max(max_score, (score - lst[i][0]))
        return
    for j in range(N):
        if visited[j] != 1:
            dfs(j)
            visited[j] = 0
            s.pop()
            score -= lst[j][0]
            cal_sum -= lst[j][1]




T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    lst.sort(key=lambda x: x[0]/x[1], reverse=True)
    s = []
    cal_sum, score, max_score = 0, 0, -1
    for i in range(N):
        dfs(i)
        visited[i] = 0
        s.pop()
        score -= lst[i][0]
        cal_sum -= lst[i][1]
    print('#{} {}'.format(tc, max_score))