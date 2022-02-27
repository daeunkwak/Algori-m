"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 문자열 반복
description : 구현, 문자열

"""


# Case1
# 반복 횟수와 문자열을 받을 때, 리스트 사용 ver

num = int(input())

for i in range(num):
    string = list(map(str, input().split()))
    for j in str(string[1]):
        for k in range(int(string[0])):
            print(j, end="")
    print()


# Case2
# 반복 횟수와 문자열을 받을 때, 리스트 사용 X ver

num = int(input())

for i in range(num):
    r, s = input().split()
    string = ''
    for j in s:
        string += int(r) * j
    print(string)