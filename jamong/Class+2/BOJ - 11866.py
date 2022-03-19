"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 요세푸스 문제 0
description : 구현, 자료 구조, 큐 

"""


'''
*큐 (queue)

: FIFO - First In First Out
: 먼저 들어오면 먼저 나감.

- 큐에 데이터를 넣는 것을 Enqueue
- 큐에서 데이터를 꺼내는 것을 Dequeue 


출처: https://sikaleo.tistory.com/31 [SIKALEO]


EX) 마크(head, Front) -> 태용 -> 재현 -> 도영 -> 해찬(Tail, Rear, Back)

head, Front : 데이터 나가는 쪽 (먼저 들어왔으니까 먼저 나감.)
Tail, Rear, Back : 데이터 들어오는 쪽 (나중에 들어왔으니까 뒤에 쌓임.)

출처: https://dongdongfather.tistory.com/72

'''


from collections import deque
from operator import index
import queue


N, K = map(int, input().split())

queue = deque()
result = []

for i in range(1, N+1):
    queue.append(i)

while (len(queue) != 0):
    for j in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print("<", end="")
for i in result:
    if (result.index(i) != (len(result)-1)):
        print(i, end=", ")
print("{0}>".format(result[-1]))