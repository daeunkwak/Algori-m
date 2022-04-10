"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 체스판 다시 칠하기
description : 브루트포스 알고리즘

"""


'''
*브루트포스 알고리즘

-> 모든 경우의 수 다 돌려서 최적의 해 구하기 

: 검색 대상이 되는 원본 문자열의 처음부터 끝까지 차례대로 순회하며 
문자열을 일일히 비교하는 방식

: 비교하고자 하는 문자열과 패턴을 한 칸씩 이동하면서 비교하여 일치 여부를 확인한다.

: 비교 문자가 같으면 두 문자열 모두 인덱스 한 칸씩 이동

: 비교 문자가 다르면 원본 문자열은 한 칸 뒤로 이동하고 
비교 문자열을 맨 처음으로 돌아간다.


출처 : https://wondytyahng.tistory.com/entry/%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4

'''


col, row = map(int, input().split())
ori = []

for i in range(col):
    ori.append(input())

new = []

# 모든 경우의 수 다 돌리기 위해
# 4중 for문 사용.....

for i in range(col-7):
    for j in range(row-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if ori[k][l] != 'W':
                        w = w+1
                    if ori[k][l] != 'B':
                        b = b+1
                else:
                    if ori[k][l] != 'B':
                        w = w+1
                    if ori[k][l] != 'W':
                        b = b+1
        new.append(w)
        new.append(b)

print(min(new))