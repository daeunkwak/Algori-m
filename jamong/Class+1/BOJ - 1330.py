"""
author : Cho Jayoung
github : https://github.com/cho-ja-young
title : 두 수 비교하기
description : 수학, 구현, 사칙연산

"""


A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")