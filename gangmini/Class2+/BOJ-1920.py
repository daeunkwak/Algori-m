'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 수 찾기
description : 자료 구조,이분 탐색,해시를 사용한 집합과 맵
'''

#### A를 리스트로 만들고 원소 확인 ####
'''
N = int(input())
A = set(map(int,input().split()))
M = int(input())
find_num = list(map(int,input().split()))

for i in find_num:
    if(i in A):
        print(1)
    else:
        print(0)
'''

#### A를 딕셔너리로 만들고 원소 확인(시간 단축) ####
N = int(input())
A={string:1 for string in map(int,input().split())}

M = int(input())
find_num = list(map(int,input().split()))

for i in find_num:
    if(i in A):
        print(1)
    else:
        print(0)