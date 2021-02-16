N, M = map(int, input().split(' '))
card_list = list(map(int, input().split(' ')))

cache = [0, 1, 2]
Osum = 0
Nsum = 0
for i in range(N-2):
    for j in range(1,N-1):
        for k in range(2,N):   
            if i == j or j == k or i == k:
                continue                 
            Nsum = card_list[i] + card_list[j] + card_list[k]
            if Nsum > Osum and Nsum <= M:
                Osum = Nsum
print(Osum)


