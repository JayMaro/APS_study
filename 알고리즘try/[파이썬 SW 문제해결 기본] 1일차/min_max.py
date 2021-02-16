T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    case_num = int(input())
    case_lst = list(map(int, input().split()))
    # 최댓값과 최솟값을 선언
    max_value = 0
    min_value = 1000001
    # 각 case를 돌면서 최댓값과 최솟값을 찾음
    for i in case_lst:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
	# 최댓값과 최솟값의 차이를 저장
    diff = max_value - min_value
    print(f'#{t} {diff}')
