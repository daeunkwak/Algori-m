'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 체스판 다시 칠하기
description : 브루트포스 알고리즘
'''

import sys
#보드 크기
while(1):
    N, M = map(int,input().split())
    if(8<=N,M<=50):
        break

#B:0 W:1 이라고 하면 8x8 체크판의 총 합은 32
borad_BW = list(sys.stdin.readline().strip() for _ in range(N))
'''
borad_label=[]
for i in borad_BW:
        borad_label.append(i.replace("B","0").replace("W", "1"))
print(borad_label)
'''
#모든 경우 검사
min = 100
for i in range(N-8+1): #세로에서 8개 뽑을 수 있는 경우의 수
    for j in range(M-8+1): #가로에서 8개를 뽑을 수 있는 경우의 수  #17 #B:11 W:6 => 32 32
        count_B = 0
        count_W = 0
        for k in range(8):
            print(borad_BW[i + k][j:j + 8])
            count_B += borad_BW[i + k][j:j + 8].count("B")
            count_W  += borad_BW[i + k][j:j + 8].count("W")

        print(count_B)
        print(count_W)
        if((32-count_B)+(32-count_W)<min):
            min = (32-count_B)+(32-count_W)
        print()
print(min)



