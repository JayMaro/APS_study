def union(a, b):
    p_a = find(a)
    p_b = find(b)
    if p_a != p_b:
        p[p_a] = p_b
    return


def find(num):
    while num != p[num]:
        num = p[num]
    return num


for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())
    p = list(range(V+1))
    sum_val = 0
    link_nodes = [tuple(map(int, input().split())) for _ in range(E)]
    link_nodes.sort(key=lambda x: x[2])
    cnt = 0
    for link in link_nodes:
        if find(link[0]) != find(link[1]):
            union(link[0], link[1])
            sum_val += link[2]
            cnt += 1
            if cnt == V:
                break
    print('#{} {}'.format(tc, sum_val))

