'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : ACM 호텔
description : 수학, 구현, 사칙연산
'''

#T개의 테스트셋 입력받음
#H:층 수 W:층마다 방수 N:손님 순서
T = int(input()) #테스트의 개수
#test = list({list(map(int, input().split())) for _ in range(T)})
#print(test)
for i in list:
    H, W, N = map(int, input().split())
    tu = divmod(N, H) #몫과 나머지를 튜플 형식으로 반환
    #몫+1 => 호수, 나머지 => 층수
    print(tu[1]*100+tu[0]+1)
