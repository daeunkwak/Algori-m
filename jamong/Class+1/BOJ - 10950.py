"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : A+B - 3
description : 수학, 구현, 사칙연산

"""


n = int(input())

#아래 a, b를 정수로 바꾸는 부분 한줄 정리
# a,b = map(int,input().split())

for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a+b)