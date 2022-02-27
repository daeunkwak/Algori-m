"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : OX퀴즈
description : 구현, 문자열

"""


import sys

n = int(input())
add = 0
sum = 0

for i in range(n):
    result = list(str(input()))
    for j in range(len(result)):
        if result[j] == "O":
            add += 1
            sum = sum + add
        else:
            add = 0

    print(sum)
    sum = 0
    add = 0