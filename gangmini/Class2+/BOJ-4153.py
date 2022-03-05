'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 직각삼각형
description : 수학, 기하학, 피타고라스 정리
'''

## lambda 매개변수 : 표현식
## map(함수, 리스트)
## reduce(함수, 시퀀스)

from functools import reduce
while(1):
    a, b, c = map(int, input().split())
    if(a==0&b==0&c==0):
        break
    else:
        list = [a,b,c] #각 변의 값을 리스트에 넣음
        hypo = max(list) #빗변 원소  추출
        del list[list.index(hypo)] #빗변 원소 제거
        legs =  reduce(lambda x, y: x**2 + y**2, list)
        if(hypo*hypo == legs):
            print("right")
        else:
            print("wrong")




