'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m
title : DFS와 BFS
description : 그래프,너비/깊이 탐색
'''

from collections import deque

class DFS_BFS:
    def __init__(self, graph,N):
        self.graph = graph
        self.visited = [0 for _ in range(N)]

    def init_visited(self):
        self.visited = [0 for _ in range(len(self.visited))]

    def dfs(self,start_node):
        # 시작노드 방문 처리
        self.visited[start_node - 1] = 1
        print(start_node,end=' ')

        for i in self.graph[start_node - 1]:
            if (self.visited[i - 1] == 0):  # 방문 안 한 노드
                #print(i)
                #self.visited[i - 1] = 1     # 방문처리
                self.dfs(i)

    def bfs(self,start_node):
        queue = deque([start_node])

        # 시작노드 방문 처리
        self.visited[start_node - 1] = 1
        #print(start_node, end=' ')

        while(queue):
            start_node = queue.popleft()
            print(start_node, end=' ')

            for i in self.graph[start_node - 1]:
                if(self.visited[i-1] == 0):
                    queue.append(i)
                    self.visited[i - 1] = 1

def main():
    N, M, V = map(int, input().split())

    ## 인접리스트로 그래프 구현
    graph = [[] for _ in range(N)]
    for i in range(M):
        node1, node2 = map(int, input().split())
        graph[(node1)-1].append(node2)
        graph[(node2)-1].append(node1)

    # 오름차순 정렬
    for i in range(len(graph)):
        graph[i].sort()
    #print(graph)

    d = DFS_BFS(graph,N)

    d.dfs(V)
    d.init_visited()
    print()
    d.bfs(V)


if __name__ == '__main__':
    main()


