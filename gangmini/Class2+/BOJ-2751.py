'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 수 정렬하기2
description : 정렬
'''

##input()으로 하면 시간포과...!!!sys 사용해야 함...

import sys
N = int(sys.stdin.readline())
num_list = list(int(sys.stdin.readline()) for _ in range(N))
num_list.sort()
for i in num_list:
    print(i)
    

'''
N = int(input())
num_list = list(input() for _ in range(N))
num_list = sorted(num_list,key = lambda x : int(x))
for i in num_list:
    print(i)

'''