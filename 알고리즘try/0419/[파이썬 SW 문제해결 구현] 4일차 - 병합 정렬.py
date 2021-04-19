def merge_sort(lst):
    global cnt  # 경우의 수 저장 변수를 전역 변수로 선언
    if len(lst) == 1:  # 만약 배열 길이가 1인 경우 그대로 반환
        return lst
    idx = len(lst)//2  # 리스트를 반으로 나누는 index
    left = merge_sort(lst[:idx])  # 왼쪽 배열
    right = merge_sort(lst[idx:])  # 오른쪽 배역
    if left[-1] > right[-1]:
        cnt += 1  # 만약 왼쪽 배열 마지막 값이 오른쪽 배열 마지막 값 보다 크다면 cnt 1 증가
    i, j = 0, 0  # 각각의 배열이 가르키고 있는 위치를 나타날 index들
    tmp = []  # 합쳐진 배열을 저장할 배열
    while True:
        if left[i] > right[j]:  # 오른쪽 항목이 왼쪽보다 작다면
            tmp.append(right[j])  # 오른쪽 항목 추가
            j += 1  # 오른쪽 index 증가
            if j == len(right):  # 만약 오른쪽 index 크기를 넘어간다면 break
                break
        else:  # 왼쪽 항목이 더 작다면
            tmp.append(left[i])  # 왼쪽 항목 추가
            i += 1  # 왼쪽 index 증가
            if i == len(left):  # 만약 왼쪽 index 크기를 넘어간다면 break
                break
    while i < len(left):  # 남아 있는 index 만큼 모두 추가
        tmp.append(left[i])
        i += 1
    while j < len(right):  # 남아 있는 index 만큼 모두 추가
        tmp.append(right[j])
        j += 1

    return tmp  # 합쳐진 배열 반환


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0  # 경우의 수 저장 변수
    print('#{} {} {}'.format(tc, merge_sort(lst)[N//2], cnt))
