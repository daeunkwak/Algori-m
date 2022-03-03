'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 직각삼각형
description : 수학, 기하학, 피타고라스 정리
'''

from functools import reduce
while(1):
    a, b, c = map(int, input().split())
    if(a==0&b==0&c==0):
        break
    else:
        list = [a,b,c]
        key = max(list)
        if(key*key == reduce(lambda x, y: x * y, list[-list.index(key)])):
            print("Right")
        else:
            print("Wrong")




