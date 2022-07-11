'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 숫자카드2
description : 자료 구조,정렬,이분 탐색,해시를 사용한 집합과 맵
'''

##성공 but, 시간 오래 걸림##

N = int(input())
s_card = list(map(int,input().split()))

card_dict={}
for i in s_card:
    if(i in card_dict): #찾고자 하는 키가 있음
        card_dict[i]=card_dict[i]+1
    else:
        card_dict[i] = 1



M = int(input())
num = list(map(int,input().split()))

for i in num:
    if(card_dict.get(i)==None):
        print(0,end=" ")
    else:
        print(card_dict.get(i),end=' ')




'''
for i in num: #시간초과
    count=0
    for j in range(N):
        if(s_card[j]==i):
            count=count+1
    print(count,end=" ")
'''