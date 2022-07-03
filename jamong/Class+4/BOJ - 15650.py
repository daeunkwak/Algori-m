"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : N과 M (2)
description : 백트래킹
"""

'''
** 백트래킹

: 돌다가 아닌 것 같을 때, 왔던 길로 다시 되돌아가
다른 경로로 가는 방법

: 재귀로 구현하는 것이 보통의 경우이며, 조건이 맞지 않으면 종료!

: DFS 깊이우선탐색 을 기반으로 한다.

'''

'''
** "join" in python

1) ".join(리스트)

: 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환

=> 구분자가 그냥 공백인 것과 같다.


2) '구분자'.join(리스트)

: 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.

*** '_'.join(['a', 'b', 'c']) 라 하면,

==> "a_b_c" 와 같은 형태로 문자열을 만들어서 반환



출처: https://blockdmask.tistory.com/468 [개발자 지망생:티스토리]

'''


N, M = map(int, input().split())

num_list = []

def dfs(start):
    if len(num_list) == M:
        print(' '.join(map(str,num_list)))
        return
    
    for i in range(start, N+1):
        if i not in num_list:
            num_list.append(i)
            dfs(i+1)
            num_list.pop()
dfs(1)