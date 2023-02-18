'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m
title : 미로탐색
description : 그래프,너비탐색
'''


import queue

def main():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().rstrip())))  # 줄바꿈 문자 제거

    # 상하좌우
    dx = [-1, 1, 0, 0]  # 좌표에서 (0,1)은 행렬에서 [1,0] y축이 행, x축이 열
    dy = [0, 0, -1, 1]

    # -> 하상우좌

    def bfs(x, y):
        que = queue.Queue()
        que.put([x, y])

        while (not que.empty()):  # 큐가 빌때까지 반복
            x, y = que.get()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # print(f'({nx},{ny})')

                if (0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1):
                    # 해당 좌표에 길이 존재하고 도착지점을 넘지 않는지 확인
                    que.put([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1
                    # 조건절 -> 같은 좌표 2번 이상 지나기 불가능
                    # 해당 좌표에 도달하기 위해 현재까지 이동한 최소 칸수 표시

        return graph[N - 1][M - 1]

    print(bfs(0, 0))


if __name__ == '__main__':
    main()