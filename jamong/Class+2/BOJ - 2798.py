"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 블랙잭
description : 브루트포스 알고리즘

"""


n, m = map(int, input().split())

nums = list(map(int, input().split()))

sum = 0

# 처음부터 끝까지 다 비교
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (nums[i] + nums[j] + nums[k] > sum) and (nums[i] + nums[j] + nums[k] <= m):
                sum = nums[i] + nums[j] + nums[k]

print(sum)

'''
<< 관련 파이썬 개념 >>

*브루트포스 알고리즘이란?
 
-> 검색 대상이 되는 원본 문자열의 처음부터 끝까지 차례대로 
순회하며 문자들을 일일이 비교하는 방식의 알고리즘 

출처: https://wondytyahng.tistory.com/entry/%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4

'''