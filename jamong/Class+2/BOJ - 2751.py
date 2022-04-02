"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 수 정렬하기 2
description : 정렬

"""


# input과 print를 사용했더니 자꾸 시간 초과가 떠서
# sys.std ~
# sys.stdout ~ 
# 으로 바꿨다. 

import sys

N = int(input())
list = []

for i in range(N):
    list.append(int(sys.stdin.readline()))

list.sort()

for j in list:
    sys.stdout.write(str(j)+"\n")