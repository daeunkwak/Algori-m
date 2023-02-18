'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m
title : 안전영역
description : 브루트포스,그래프,너비/깊이 탐색
'''

from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
HeightArr = [list(map(int, input().split())) for _ in range(N)]

# 안전 지대의 기준 높이를 저장
HeightSet = sum(HeightArr, [])
HeightSet = set(HeightSet)
HeightSet.add(0)

areaList = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for s in HeightSet:
    area = 0
    safeArr = [arr[:] for arr in HeightArr]  #deepcopy()는 슬라이싱에 비해 7배 가량 느리다

    for i in range(N):
        for j in range(N):
            que = deque()
            if (safeArr[i][j] > s):
                que.append([i, j])
                safeArr[i][j] = 0
                area += 1

            while(que):
                x, y = que.popleft()

                for n in range(4):
                    nx = x + dx[n]
                    ny = y + dy[n]

                    if (0 <= nx < N and 0 <= ny < N and safeArr[nx][ny] > s):
                        # 해당 좌표에 길이 존재하고 도착지점을 넘지 않는지 확인
                        que.append([nx, ny])
                        safeArr[nx][ny] = 0

    if (area > 0): # 기준 높이인 s 에서 안전영역이 있는 경우
        areaList.append(area)

if (areaList):
    print(max(areaList))