"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 최댓값
description : 구현

"""


nums = []

for i in range(9):
    nums.append(int(input()))

max = nums[0]

for i in nums[1:]:
    if i >= max:
        max = i

print(max)
print(nums.index(max)+1)