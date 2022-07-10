'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 요세푸스 문제 0
description : 구현, 자료구조, 큐
'''

from collections import deque

N, K = map(int, input().split())

deq = deque()      # deque객체 생성
for i in range(N): # deque에 1~N까지 삽입
    deq.append(i+1)

for i in range(N):
    deq.rotate(-(K-1)) #3번째 요소가 가장 앞에 오도록 rotation
    if (i == 0):
        print('<',end="")
    print(deq.popleft(),end="")
    if (i == N-1):
        print('>')
        break
    print(', ',end="")
