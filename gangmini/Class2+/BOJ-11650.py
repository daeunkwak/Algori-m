'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 좌표 정렬하기
description : 정렬
'''

import sys
N = int(sys.stdin.readline())
xy_list = list(sys.stdin.readline().split() for _ in range(N))
#y좌표 기준 정렬 -> x좌표 기준 정렬
xy_list = sorted(xy_list,key = lambda x : int(x[1]))
xy_list = sorted(xy_list,key = lambda x : int(x[0]))
for i in xy_list:
    print(int(i[0]),int(i[1]))

