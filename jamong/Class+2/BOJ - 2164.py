"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 카드2
description : 자료 구조, 큐

"""

from collections import deque


num = int(input())

queue = deque()

for i in range(1, num+1):
    queue.append(i)

while (len(queue) > 1):
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())
