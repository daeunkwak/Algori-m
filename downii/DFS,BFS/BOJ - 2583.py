"""
author : Kwak Daeun
github : https://github.com/daeunkwak

title : 영역 구하기
description : 그래프, DFS, BFS
"""

from collections import deque
import sys

M, N, K = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    cnt = 0
    graph[y][x] = 1
    while dq:
        y, x = dq.popleft()
        cnt += 1
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            # 직사각형부분 1로 처리
            if 0 <= ny < M and 0 <= nx < N:
                if graph[ny][nx] == 0:
                    dq.append((ny, nx))
                    graph[ny][nx] = 1
    return cnt

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
res = []
cnt = 0

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            res.append(bfs(i, j))

print(len(res))
print(*sorted(res))




