"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 1, 2, 3 더하기
description : 다이나믹 프로그래밍

"""

import sys

addlist = [0]*11
addlist[1] = 1
addlist[2] = 2
addlist[3] = 4

for i in range (4, 11):
    addlist[i] = sum(addlist[i-3:i])

T = int(sys.stdin.readline())

for _ in range(T):
    print(addlist[int(sys.stdin.readline())])
