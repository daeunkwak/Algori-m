"""
author : Kwak Daeun
github : https://github.com/daeunkwak

title : 스택 수열
description : 자료구조, 스택
"""

n = int(input())
des = []
stackk = []

for i in range (n) :
    des.append(input())

j = 0
for i in range (n) :
    if i != des[j] :
        stackk.append(i)
        print("+")
    else :
        stackk.append(i)
        print("+")
        stackk.pop()
        print("-")
        if des[j + 1] > des[j] :
            continue
        else :
            if des[j + 1] == stackk[-1] :
                stackk.pop()
                print("-")
                # 이 구조를 재귀함수로 표현할 수 있지 않을까..?

# 진짜 멍청해졌네...ㅋ...ㅋ











