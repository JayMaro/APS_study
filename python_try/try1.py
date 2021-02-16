
T = int(input())
i_lst = []
for t in range(T):
    age, name = input().split()
    i_lst.append([int(age), name])
    
i_lst.sort(key=lambda x:x[0])
for i in i_lst:
    print(i[0], i[1])
    

