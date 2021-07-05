def solution(n):
    nn = n*(n+1)//2
    arr = [0]*nn
    now_type = 1
    now = 1
    i = 0
    j = 0
    while now <= nn:
        if now_type == 1:

            i += j
            if i >= nn or arr[i] != 0:
                now_type = 2
                i -= j
                continue

            arr[i] = now
            j += 1
            now += 1

        elif now_type == 2:

            i += 1

            if i >= nn or arr[i] != 0:
                now_type = 3
                i -= 1
                continue

            arr[i] = now
            now += 1

        elif now_type == 3:

            i -= j

            if i <= 0 or arr[i] != 0:
                now_type = 1
                i += j
                continue

            arr[i] = now
            now += 1
            j -= 1

    return arr