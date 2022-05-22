"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 직사각형에서 탈출
description : 수학, 기하학

"""

x, y, w, h = map(int, input().split())

# x 와 y 는 그 자체로 거리가 됨.
# w 와 h 는 각각 w-x, h-y로 거리를 표현할 수 있음.

# 최솟값이므로 min 사용

print(min(x, y, w-x, h-y))