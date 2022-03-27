'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 덱
description : 자료구조, 덱
'''

#덱: 일차원 선형 자료구조, 스택과 큐 연산을 모두 지원하는 양방향 연결리스
#파이썬에서는 collections 모듈에 deque 클래스로 구현

deque=[]

#맨 앞에 원소 추가하고 싶으면 insert(인덱스,원소)
def push_front(x):
    deque.insert(0,x)

def push_back(x):
    deque.append(x)

def pop_front():
    if(len(deque)==0):
        print(-1)
        return;
    print(deque[0])
    deque.pop(0)

def pop_back():
    if(len(deque)==0):
        print(-1)
        return;
    print(deque[len(deque)-1])
    deque.pop(len(deque)-1)

def size():
    print(len(deque))

def empty():
    if(len(deque)==0):
        print(1)
    else:
        print(0)

def front():
    if(len(deque)==0):
        print(-1)
        return;
    print(deque[0])


def back():
    if(len(deque)==0):
        print(-1)
        return;
    print(deque[len(deque) - 1])


N = int(input())
statment = [list(map(str,input().split())) for _ in range(N)]
for i in statment:
    if(i[0]=='push_back'):
        push_back(i[1])
    elif(i[0]=='push_front'):
        push_front(i[1])
    elif (i[0] == 'front'):
        front()
    elif (i[0] == 'back'):
        back()
    elif (i[0] == 'size'):
        size()
    elif (i[0] == 'empty'):
        empty()
    elif (i[0] == 'pop_front'):
        pop_front()
    elif (i[0] == 'pop_back'):
        pop_back()

