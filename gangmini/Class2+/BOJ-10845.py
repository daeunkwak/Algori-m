'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 큐
description : 자료구조, 큐
'''



def push(x):
    qqu.append(x)

def pop(): #제일 앞의 값을 지우면 어떻게 되는지 확인
    if(len(qqu)==0):
        print(-1)
    else:
        print(qqu[0])
        qqu.pop(0)

def size():
    print(len(qqu))

def empty():
    if(len(qqu)==0):
        print(1)
    else:
        print(0)

def front():
    if(len(qqu)==0):
        print(-1)
    else:
        print(qqu[0])

def back():
    if (len(qqu) == 0):
        print(-1)
    else:
        print(qqu[len(qqu)-1])

qqu = []
N = int(input())
statment = [list(map(str,input().split())) for _ in range(N)]

for i in statment:
    if(i[0]=='push'):
        push(i[1])
    elif(i[0]=='pop'):
        pop()
    elif (i[0] == 'size'):
        size()
    elif (i[0] == 'empty'):
        empty()
    elif (i[0] == 'front'):
        front()
    elif (i[0] == 'back'):
        back()