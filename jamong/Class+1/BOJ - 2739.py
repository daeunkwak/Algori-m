"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 구구단
description : 수학, 구현, 사칙연산

"""


n = int(input())

for i in range(1, 10):
    print("{0} * {1} = {2}".format(n, i, n*i))