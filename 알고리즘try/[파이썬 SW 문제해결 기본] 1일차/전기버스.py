T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    K, N, M = map(int, input().split())
    stop_lst = [0]*(N+1)
    stop_lst_num = list(map(int, input().split()))
    # 입력받은 리스트를 각 인덱스에 1로 저장
    for lst_num in stop_lst_num:
        stop_lst[lst_num] = 1
    # 전기 버스의 운행이 가능한가를 나타내는 변수 선언
    possible = True
    # i를 선언
    i = K
    # 충전횟수 선언
    cnt = 0
    while i < N+1:
        # 마지막 정류장이라면 break(while문 break)
        if i == N:
            break
        # 1씩 빼기위해 미리 1을 더해줌
        i += 1
        # 1씩 K번 빼면서 충전소 유무를 확인
        for x in range(K):
            i -= 1
            # 충전소가 잇다면 cnt를 1 증가시키고 계속 진행(for문 break)
            if stop_lst[i] == 1:
                cnt += 1
                break
		# 만약 반복문을 다 돌았다면 충전소가 없는 것이므로 possible = False 후 중지 (while문 break)
        else:
            possible = False
            break
		# i에 K를 더해서 다음 반복 진행
        i += K

	# possible이라면 cnt 출력 그렇지 않다면 0을 출력
    if possible:
        print(f'#{t} {cnt}')
    else:
        print(f'#{t} 0')
