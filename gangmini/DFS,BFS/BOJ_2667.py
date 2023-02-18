'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m
title : 단지번호붙이기
description : 그래프,너비/깊이 탐색
'''

import queue

N = int(input())
houseArr = [list(map(int, input().rstrip())) for _ in range(N)]

# bfs 로 구현 (재귀호출 부담을 줄이기 위함)
# 큐에 추가될 때마다 단지내 아파트 카운트 +1
# while문 끝날 때마다 단지 카운트 +1

def bfs():
    town = 0
    aptList = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            que = queue.Queue()
            apt = 0
            if (houseArr[i][j] == 1):
                que.put([i, j])
                houseArr[i][j] += 1
                apt += 1
                town += 1

            # while 문이 끝나면 한 단지 탐색 완료
            while (not que.empty()):
                x, y = que.get()

                for n in range(4):
                    nx = x + dx[n]
                    ny = y + dy[n]

                    if (0 <= nx < N and 0 <= ny < N and houseArr[nx][ny] == 1):
                        # 해당 좌표에 길이 존재하고 도착지점을 넘지 않는지 확인
                        que.put([nx, ny])
                        houseArr[nx][ny] += 1
                        apt += 1

            if(apt > 0):
                aptList.append(apt)

    print(town)
    aptList.sort()
    for i in aptList:
        print(i)

bfs()
