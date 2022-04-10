'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 큐
description : 자료구조, 큐
'''

qqu = []
N = int(input())
statment = [list(map(str,input().split())) for _ in range(N)]

def push(x):
    qqu.append(x)

def pop():
    if(len(qqu)==0):
        return -1
    else:
        print(qqu[0])
        qqu.pop(0)

def size():
    print(len(qqu))

def empty():
    if(len(qqu)==0):
        return 1
    else:
        return 0

def front():
    if(len(qqu)==0):
        return -1
    else:
        print(qqu[0])

def back():
    if (len(qqu) == 0):
        return -1
    else:
        print(qqu[len(qqu)-1])


