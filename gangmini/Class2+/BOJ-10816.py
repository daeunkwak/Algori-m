'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 숫자카드2
description : 자료 구조,정렬,이분 탐색,해시를 사용한 집합과 맵
'''

N = int(input())
s_card = list(map(int,input().split()))

M = int(input())
num = list(map(int,input().split()))


for i in num:
    count=0
    for j in range(N):
        if(s_card[j]==i):
            count=count+1
    print(count,end=" ")