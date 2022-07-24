"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 점프 점프
description : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

"""

from collections import deque
from unittest import result

n = int(input()) # 돌다리의 돌 개수 n
Ai = list(map(int, input().split())) # 그 위치에서 점프할 수 있는 거리
s = int(input())-1 # 출발점 

graph = [ 0 for _ in range(n)]

queue = []

def BFS(s):
    global result
    queue.append(s)
    graph[s] = 1
    result += 1

    while queue:
        node = queue[0]
        del queue[0]

        for i in [-Ai[node], Ai[node]]:
            jump = node + i

            if (0 <= jump < n) and (graph[jump] == 0):
                queue.append(jump)
                result += 1
                graph[jump] = 1


result = 0 # 방문 개수
BFS(s)

print(result)