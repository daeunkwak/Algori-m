"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

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