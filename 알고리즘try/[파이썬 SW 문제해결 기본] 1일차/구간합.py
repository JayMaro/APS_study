T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    N, M = map(int, input().split())
    i_lst = list(map(int, input().split()))
    # 최댓값 최솟값 선언
    min_val = 1000000000
    max_val = 0
    # range(0, N-M+1) -> 반복 횟수를 길이만큼 줄임
    for i in range(0, N-M+1):
        # 숫자들의 합을 선언하고 합하는 숫자의 갯수만큼 반복 덧셈
        lst_sum = 0
        for j in range(M):
            lst_sum += i_lst[i+j]
        # 최댓값과 최솟값 비교
        if lst_sum > max_val:
            max_val = lst_sum
        if lst_sum < min_val:
            min_val = lst_sum
    # 최댓값과 최솟값의 차이를 저장
    lst_diff = max_val - min_val

    print(f'#{t} {lst_diff}')
