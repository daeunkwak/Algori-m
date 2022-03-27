'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 스택
description : 자료구조, 스택
'''


stack=[]

#맨 앞에 원소 추가하고 싶으면 insert(인덱스,원소)
def push(x):
    stack.append(x)

def pop():
    if (len(stack) == 0):
        print(-1)
        return;
    print(stack[len(stack)-1])
    stack.pop(len(stack)-1)

def size():
    print(len(stack))

def empty():
    if(len(stack)==0):
        print(1)
    else:
        print(0)

def top():
    if (len(stack) == 0):
        print(-1)
        return;
    print(stack[len(stack)-1])

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
    elif (i[0] == 'top'):
        top()
