"""
author : Kwak Daeun
github : https://github.com/daeunkwak

title : 유기농 배추
description : 그래프, BFS, DFS
"""

import sys
sys.setrecursionlimit(10000)

def dfs(x, y) :
    # 범위 확인
    if x < 0 or x >= N or y < 0 or y >= M :
        return False

    if graph[x][y] == 1 :
        graph[x][y] = 0

        # 배추의 상하좌우 탐색
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

T = int(input())

for _ in range (T) :
    M, N, K = map(int, input().split())
    result = 0

    graph = [[0 for _ in range(M)] for _ in range(N)]

    # 배추위치 입력
    for i in range (K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if dfs(i, j) is True :
                result += 1
    print(result)




