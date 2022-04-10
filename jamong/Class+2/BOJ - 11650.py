"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 좌표 정렬하기
description : 정렬

"""

N = int(input())
n_list = []

for _ in range(N):
    xy = list(map(int, input().split()))
    n_list.append(xy)

n_list.sort(key=lambda x: (x[0], x[1]))

for i in n_list:
    print(i[0], i[1])

