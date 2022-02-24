from collections import deque

T = int(input())
for i in range (T) :
    N, M = map(int, input().split())
    print_list = input().split(' ')
    dq = deque(print_list)
    
    count = 1
    for j in range (1, N + 1) :
        print(dq)
        if dq[0] < dq[j] :
            dq.append(dq[0])
            dq.popleft()
            print(dq)

    

    




