T = int(input())
for tc in range(T):
    N = int(input())
    cloth_dict = {}
    for _ in range(N):
        cloth, kind = input().split()
        if cloth_dict.get(kind, -1) == -1:
            cloth_dict[kind] = [cloth]
        else:
            cloth_dict.get(kind).append(cloth)

    res = 1
    clothes = cloth_dict.values()
    for cloth in clothes:
        res *= len(cloth)+1
    print(res-1)
