def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = len(lst)//2
    left, right, equal = [], [], []
    for i in range(len(lst)):
        if lst[i] > lst[pivot]:
            right.append(lst[i])
        elif lst[i] < lst[pivot]:
            left.append(lst[i])
        else:
            equal.append(lst[i])

    return quick_sort(left) + equal + quick_sort(right)

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    std = len(lst)//2
    left = lst[:std]
    right = lst[std:]
    merge_sort(left)
    merge_sort(right)

    i, j, k= 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            k += 1
            i += 1
        else:
            lst[k] = right[j]
            k += 1
            j += 1

    if i == len(left):
        while j < len(right):
            lst[k] = right[j]
            k += 1
            j += 1
    if j == len(right):
        while i < len(left):
            lst[k] = left[i]
            k += 1
            i += 1
    return lst


N, K = map(int, input().split())
num_lst = list(map(int, input().split()))
print(merge_sort(num_lst)[K-1])