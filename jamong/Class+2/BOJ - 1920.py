"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 수 찾기 
description : 자료 구조, 이분 탐색, 해시를 사용한 집합과 맵
"""

# 1번 풀이 : 이분 탐색 

from sys import stdin, stdout

N = int(input())
n_list = sorted(map(int,stdin.readline().split()))

M = int(input())
m_list = map(int,stdin.readline().split())

def binary_fun(t, n_list, start, end):
    if start > end:
        return 0
    M = (start + end)//2
    if t == n_list[M]:
        return 1
    elif t < n_list[M]:
        return binary_fun(t, n_list, start, M-1)
    else:
        return binary_fun(t, n_list, M+1, end)

for t in m_list:
    start = 0
    end = len(n_list)-1
    print(binary_fun(t,n_list,start,end))



# 2번 풀이 : 집합 SET 사용

# 사실 집합이 훨씬 생각하기엔 쉽다.
# 있는지 없는지 다 돌아다니지 않아도 한방에 확인 가능

for t in m_list:
    stdout.write('1\n') if t in n_list else stdout.write('0\n')