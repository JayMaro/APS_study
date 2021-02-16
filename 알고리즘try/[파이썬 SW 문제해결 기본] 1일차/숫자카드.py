T= int(input())

for t in range(1, T+1):
    # 입력받는 부분
    card_lst = [0]*10
    card_num = int(input())
    card = int(input())
    # 입력받은 숫자를 10으로 나눈 나머지들을 각각의 인덱스로 1씩 올리며 저장
    for i in range(card_num):
        card_lst[card % 10] += 1
        card = card // 10
	# 최댓값과 최댓값의 인덱스 값을 구함
    max_card = 0
    max_idx = 0
    for i in range(10):
        if card_lst[i] >= max_card:
            max_card = card_lst[i]
            max_idx = i

    print(f'#{t} {max_idx} {max_card}')