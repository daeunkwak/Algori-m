'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 카드2
description : 자료구조, 큐
'''

N = int(input()) #정수 입력
queue = [i for i in range(N+1)] #0~N 1차원 배열
front = 0
rear = N
while(1):
    front = (front+1)%(N+1)
    if(front==rear):
        print(queue[rear])
        break
    front = (front + 1) % (N + 1)
    rear = (rear+1)%(N+1)
    queue[rear]=queue[front]