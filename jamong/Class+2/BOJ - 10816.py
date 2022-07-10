"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 숫자 카드 2
description : 자료 구조, 정렬, 이분 탐색, 해시를 사용한 집합과 맵

"""

from sys import stdin

# 처음에 숫자를 받아서 for문으로 돌려서
# 리스트에 하나하나 다 담아야 하는 것으로 생각했다...

_ = stdin.readline()  # 상근이가 가지고 있는 숫자 카드의 개수
N_list = sorted(map(int,stdin.readline().split()))  # 숫자 카드에 적혀있는 정수

_ = stdin.readline()
M_list = map(int,stdin.readline().split())  # 몇 개 가지고 있는지 구할 숫자 카드


def binary(n, N_list, start, end):
    if start > end:
        return 0
    m = (start+end)//2  # 중간값
    if n == N_list[m]:  # n을 리스트의 중간값과 비교 
        return N_list[start:end+1].count(n)  # 몇 개가 있는지 센다 
    elif n < N_list[m]:
        return binary(n, N_list, start, m-1)
    else:
        return binary(n, N_list, m+1, end)


n_dic = {}  # dictionary

for n in N_list:
    start = 0
    end = len(N_list) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N_list, start, end)

# 각 수가 적힌 숫자 카드를 몇 개 가지고 있는지
print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M_list ))





# 도움받은 곳

# https://chancoding.tistory.com/45
