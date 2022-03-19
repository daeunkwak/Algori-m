"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 단어 정렬
description : 문자열, 정렬

"""


num = int(input())
num_list = []

for i in range(num):
    num_list.append(input())

num_set = list(set(num_list)) # 중복 없애기 

num_set.sort() # 알파벳 순으로 정렬
num_set.sort(key=len) # 문자열 길이 순으로 정렬

for j in num_set:
    print(j)