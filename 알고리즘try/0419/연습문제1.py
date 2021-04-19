lst = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
# lst = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
def quick_sort(l, r):
    if l >= r:
        return
    p = lst[l]
    i, j = l+1, r
    while i <= j:
        if lst[i] <= p:
            i += 1
            continue
        if lst[j] >= p:
            j -= 1
            continue
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    quick_sort(l, j-1)
    quick_sort(j+1, r)

quick_sort(0, len(lst)-1)
print(lst)