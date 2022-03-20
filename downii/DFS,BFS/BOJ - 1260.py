"""
author : Kwak Daeun
github : https://github.com/daeunkwak

title : DFS와 BFS
description : 그래프, DFS, BFS
"""

from collections import deque

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] is False:
            dfs(graph, i, visited)


def bfs(graph, v, visited) :
    visited[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] is False:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)
graph.append([])

for i in range (M) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range (1, N + 1) :
    graph[i].sort()

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)








