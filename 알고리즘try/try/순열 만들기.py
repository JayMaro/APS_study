def perm(n, k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [1, 2, 3]
perm(len(arr), 0)