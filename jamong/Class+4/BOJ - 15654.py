"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : N과 M (5)
description : 백트래킹

"""

# N개의 자연수 중에서 M개를 고른 수열
N, M = map(int, input().split())

n_list = list(map(int, input().split()))
n_list.sort()  # 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

stack = []

def back_tr():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    else: 
        for i in n_list:
            # for문을 돌면서 없는 숫자를 append 
            if i not in stack:
                stack.append(i)
                back_tr()
                stack.pop()

back_tr()



# 참고

# https://wlstyql.tistory.com/62
# https://jjyoung.tistory.com/79