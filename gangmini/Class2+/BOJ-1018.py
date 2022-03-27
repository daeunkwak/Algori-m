'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 체스판 다시 칠하기
description : 브루트포스 알고리즘
'''

##다으니=>체스판의 경우 2가지를 미리 만들어놓고 비교

import sys
#보드 생성
while(1):
    N, M = map(int,input().split(" "))
    if(8<=N,M<=50):
        break
borad = list(sys.stdin.readline().strip() for _ in range(N))

#모든 경우 검사
min = 100
for i in range(N-7): #세로에서 8개 뽑을 수 있는 경우의 수
    for j in range(M-7): #가로에서 8개를 뽑을 수 있는 경우의 수
        count_B = 0
        count_W = 0
        for n in range(8):
            for m in range(8):
                # 다른 개수 세기(버전별로)
                if (n % 2 == 0):  # 짝수
                    if(borad[i + n][m] !="B"):
                        count_B += 1
                    if (borad[i + n][m] != "W"):
                        count_W += 1

                else:
                    if (borad[i + n][m] != "W"):
                        count_B += 1
                    if (borad[i + n][m] != "B"):
                        count_W += 1


        print(count_B,count_W)
        print()
        #count_B, count_W 중 더 작은 것

        #min보다 더 작은지 확인

'''
min = 100
for i in range(N-8+1): #세로에서 8개 뽑을 수 있는 경우의 수
    for j in range(M-8+1): #가로에서 8개를 뽑을 수 있는 경우의 수  #17 #B:11 W:6 => 32 32 // 37->32  27+5=32
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
'''


