"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : A+B - 5
description : 수학, 구현, 사칙연산

"""


import sys

while (True):
    a,b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    print(a+b)