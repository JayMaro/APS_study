import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    input_lst = list(input())
    temp_lst = []
    result = []
    for i in input_lst:
        if i == '<':
            if result:
                temp_lst.append(result.pop())
            else:
                continue
        elif i == '>':
            if temp_lst:
                result.append(temp_lst.pop())
            else:
                continue
        elif i == '-':
            if result:
                result.pop()
            else:
                continue
            
        else:
            result.append(i)
    temp_lst.reverse()
    for x in temp_lst:
        result.append(x)
    print(''.join(result))

    







    