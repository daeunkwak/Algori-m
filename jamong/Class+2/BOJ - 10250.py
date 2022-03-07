"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : ACM 호텔
description : 수학, 구현, 사칙연산 

"""


# T 개의 테스트 데이터

# H : 호텔의 층 수
# W : 각 층의 방 수
# N : 몇 번째 손님인지


# room 을 문자열로 잡아두고 H와 W를 더해서 
# 호수를 만드는 것으로 생각했다. 


# 첫번째 경우
# 런타임 에러남

'''
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    for j in range(1, N+1):
        h = j
        w = j // H + 1
        if j > H:
            h = j % H
            if h == 0:
                h = H
        if j // H == 0:
            w -= 1

    if w < 10:
        w = '0' + str(w)
    room = str(h) + w
    print(room)

'''


# 두번째 경우
# 불필요한 부분 제거 
# 런타임 에러 

'''
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    h = N % H
    if h == 0:
        h = H 
    w = N // H + 1
    if N // H == 0:
        w -= 1

    if w < 10:
        w = '0' + str(w)
    room = str(h) + w
    print(room)

'''


# 세번째 경우
# print 방법 수정
# 틀림

'''
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    h = N % H
    if h == 0:
        h = H 
    w = N // H + 1
    if N // H == 0:
        w -= 1      

    print(f'{h*100+w}')

'''


# 네번째 경우
# 호수 계산 코드 수정 
# 맞았음

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    w = N // H + 1
    h = N % H
    if h == 0: 
        h = H 
        w -= 1       

    print(f'{h*100+w}')