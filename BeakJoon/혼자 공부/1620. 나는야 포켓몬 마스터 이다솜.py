import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pocket_name = {}
pocket_num = {}
for i in range(1, N+1):
    name = input().rstrip()
    pocket_num[i] = name
    pocket_name[name] = i

for i in range(M):
    inp = input().rstrip()
    if inp.isdigit():
        print(pocket_num[int(inp)])
    else:
        print(pocket_name[inp])

