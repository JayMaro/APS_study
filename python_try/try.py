# import sys
# sys.stdin = open("input.txt", "r")
# 입력받은 길이만큼 
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# 입력받은 길이 -2 만큼 2번 반복

def snail(num_lst, j, num):
    while True:
        
        for i in range(num-j):
            num_lst[i+j][num-1+j] = num_lst[j][num-1+j] + i
            if num_lst[j][num-1] + i == num**2:
                return num_lst
        print(num_lst)

        for i in range(num-j):
            num_lst[num-1-j][num-1-i-j] = num_lst[num-1-j][num-1-j] + i
            if num_lst[num-1][num-1] + i == num**2:
                return num_lst
        print(num_lst)
        for i in range(num-j-1):
            num_lst[num-1-i][j] = num_lst[num-1][j] + i
            if num_lst[num-1][j] + i == num**2:
                return num_lst
        print(num_lst)
        for i in range(num-j-1):
            num_lst[j+1][j+i] = num_lst[j+1][j] + i
            if num_lst[j+1][j] + i == num**2:
                return num_lst
        print(num_lst)
    
        j += 2

T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    num = int(input())
    num_lst = [[0 for i in range(num)] for j in range(num)]
    
    for i in range(num):
        num_lst[0][i] = i+1
    
    num_lst = snail(num_lst, 0, num)
    print(**num_lst)
    
    



