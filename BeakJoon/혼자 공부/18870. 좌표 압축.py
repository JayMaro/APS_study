import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
location_lst = list(set(lst))
location_lst.sort()
location_dict = {}
for idx, num in enumerate(location_lst):
    location_dict[num] = idx
res = [0]*N
for i in range(len(lst)):
    res[i] = location_dict[lst[i]]
print(*res)