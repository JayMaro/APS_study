T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
