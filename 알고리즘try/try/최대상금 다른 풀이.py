for tc in range(1, int(input()) + 1):
    num, N = input().split()
    K = len(num)
    N = int(N)
    nums = set([num])
    res = set()

    for n in range(N):
        while nums:
            s = nums.pop()
            s = list(s)
            for i in range(K - 1):
                for j in range(i + 1, K):
                    s[i], s[j] = s[j], s[i]
                    res.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        nums, res = res, nums

    print('#{} {}'.format(tc, max(nums)))