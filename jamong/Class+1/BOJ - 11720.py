"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 숫자의 합
description : 수학, 문자열, 사칙연산

"""


# Case1

n = input()
nums = list(input())
sum = 0

for i in nums:
    sum += int(i)

print(sum)



# Case2

input()
print(sum(map(int,input())))