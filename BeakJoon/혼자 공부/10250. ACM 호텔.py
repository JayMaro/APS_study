T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    cnt = 0
    for j in range(M):
        for i in range(N):
            cnt += 1
            if cnt == K:
                floor = str(i+1)
                room_num = str(j+1)
                if len(room_num) == 1:
                    room_num = '0' + room_num
                res = floor + room_num
    print(res)
