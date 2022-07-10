'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 체스판 다시 칠하기
description : 브루트포스 알고리즘
'''

##다으니=>체스판의 경우 2가지를 미리 만들어놓고 비교

mini=64 #8x8 체스판 모두 바꾸는 경우가 최대
str1 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'
str2 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'

def compare_str(chass, str):
    global mini #전역변수 사용 위해 global 선언
    count=0
    #8번씩 문자 8개 비교
    for i in range(64):
        if(chass[i]!=str[i]):
            count = count+1
    if(count < mini):
        mini = count

#보드 생성
borad=[]
while(1):
    N, M = map(int,input().split(" "))
    if(N<0 |N<8 | M>50):
        print("N, M은 8이상 50이하")
        break
    else:
        for i in range(N):
            borad.append(input())
        break
print(borad)

for i in range(N-7):
    for j in range(M-7):
        chass=''
        for k in range(8):
            chass = chass+borad[i:i+8][k][j:j+8]
        #print(chass)
        compare_str(chass, str1)  # 8x8 부분 집합
        compare_str(chass, str2)
           
print(mini)












'''
#모든 경우 검사
min = 64 #8x8 체스판 모두 바꾸는 경우가 최대
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


