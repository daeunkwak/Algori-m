"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 최소, 최대
description : 수학, 구현

"""


# Case1

import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
max = nums[0]
min = nums[0]

for i in range(n):
    if nums[i] >= max:
        max = nums[i]

    if nums[i] <= min:
        min = nums[i]

print(min, max)



# Case2

# cnt = int(input())
# numbers = list(map(int, input().split()))
# max = numbers[0]
# min = numbers[0]

# for i in numbers[1:]:
#     if i > max:
#         max = i
#     elif i < min:
#         min = i

# print(min, max)​


# Case3

# cnt = int(input())
# numbers = list(map(int, input().split()))
# print(min(numbers),max(numbers))