"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 집합
description : 구현, 비트마스킹
"""

'''
**비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- all: S를 {1, 2, ..., 20} 으로 바꾼다.
- empty: S를 공집합으로 바꾼다. 

'''

# 틀림

# import sys

# M = int(input())
# s = set()

# for i in range(M):
#     line = sys.stdin.readline().strip().split()

#     if len(line) == 1:
#         if line[0] == 'all':
#             s = set([i for i in range(1, 21)])
#         else:
#             s = set() # empty
#         continue

#     command, target = line[0], line[1]
#     target = int(target)

#     if command == 'add':
#         s.add(target)
#     elif command == 'check':
#         if (target in s):
#             print("1")
#         else:
#             print("0")
#     elif command == 'toggle':
#         if target in s:
#             s.discard(target)
#         else:
#             s.add(target)


# 두번째 시도

import sys

M = int(input())
s = set()

for i in range(M):
    line = sys.stdin.readline().strip().split()

    if len(line) == 1:
        if line[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set() # empty
        continue

    command, target = line[0], line[1]
    target = int(target)

    if command == 'add':
        s.add(target)
    elif command == 'check':
        if (target in s):
            print("1")
        else:
            print("0")
    elif command == 'remove':
        s.discard(target)
    elif command == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)