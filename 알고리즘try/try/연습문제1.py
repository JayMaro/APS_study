def insert_search(lst, idx):
    if idx == len(lst)-1:
        return lst
    min_idx = idx
    for i in range(idx, len(lst)):
        if lst[i] < lst[min_idx]:
            min_idx = i
    lst[idx], lst[min_idx] = lst[min_idx], lst[idx]
    return insert_search(lst, idx+1)


a = [2, 10, 1, 3, 14, 5, 2, 2, 1]
b = insert_search(a, 0)
print(b)