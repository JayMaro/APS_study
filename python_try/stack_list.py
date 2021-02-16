N = int(input())


num_list = list(range(1,N+1))
work_list = []
stack_list = []
result = []
result_list = []

for i in range(N):
    num = int(input())
    work_list.append(num)



index = 0


for x in num_list:
    stack_list.append(x)
    result_list.append('+')
        
    while stack_list[-1] == work_list[index]:
            result.append(stack_list.pop())
            result_list.append('-')
            index += 1
            if len(stack_list) == 0:
                break
                    
            if index == N:
                print('\n'.join(result_list))
                exit(0)
    else:
        print('NO')
        exit(0)



    
       