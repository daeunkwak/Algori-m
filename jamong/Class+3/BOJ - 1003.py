"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 피보나치 함수
description : 다이나믹 프로그래밍
"""

# 1번 풀이 : 재귀함수 사용 
# 실패 -> 시간초과 

T = int(input())  # 테스트 케이스의 개수

num_0 = 0  # 0이 출력되는 횟수
num_1 = 0  # 1이 출력되는 횟수

def fibonacci(N):

    global num_0
    global num_1 
 
    if N == 0:
        num_0 += 1

        return 0

    elif N == 1:
        num_1 += 1

        return 1

    else:
        return fibonacci(N-1) + fibonacci(N-2)

 
for _ in range(T):
    N = int(input())  # 40보다 작거나 같은 자연수 또는 0
    fibonacci(N)
    print(num_0, num_1)
    num_0 = 0
    num_1 = 0



# 수정 후
# 성공 

T = int(input())  # 테스트 케이스의 개수

num_0 = [1, 0, 1]  # 0이 출력되는 횟수
num_1 = [0, 1, 1]  # 1이 출력되는 횟수

def fibonacci(N):

    num_len = len(num_0) 
 
    if N >= num_len:
        for i in range(num_len, N+1):
            num_0.append(num_0[i-1] + num_0[i-2])
            num_1.append(num_1[i-1] + num_1[i-2])
    print('{} {}'.format(num_0[N], num_1[N]))
 
for _ in range(T):
    N = int(input())  # 40보다 작거나 같은 자연수 또는 0
    fibonacci(N)


