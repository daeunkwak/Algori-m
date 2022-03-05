'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : ACM 호텔
description : 수학, 구현, 사칙연산
'''

#T개의 테스트셋 입력받음
#H:층 수 W:층마다 방수 N:손님 순서

T = int(input())
test = [list(map(int, input().split())) for _ in range(T)]
for i in test:
    tu = divmod(i[2], i[0])  #몫과 나머지를 튜플 형식으로 반환
    if(tu[1]==0): #나머지가 0이면 꼭대기층 #호수는 몫과 동일
        print(i[0] * 100 + tu[0])
    else: #몫+1 => 호수, 나머지 => 층수
        print(tu[1] * 100 + tu[0] + 1)
