"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 덩치
description : 구현, 브루트포스 알고리즘

"""

'''
** 어떤 사람의 몸무게가 x kg이고 키가 y cm
=> 이 사람의 덩치는 (x, y)로 표시

** 둘 다 커야 "덩치"가 더 크다고 말할 수 있다!

'''

N = int(input()) # 전체 사람의 수
n_list = []

for _ in range(N):
    x, y = map(int, input().split()) # 몸무게, 키
    n_list.append((x, y))

for i in n_list:
    rank = 1
    for j in n_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")