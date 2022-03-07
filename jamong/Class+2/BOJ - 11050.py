"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 이항 계수 1
description : 수학, 구현, 조합론 

"""


# 첫번째 생각
# 틀림

'''
N, K = map(int, input().split())
result = 1

for i in range(K):
    result *= N
    result /= K
    N -= 1
    K -= 1

print(int(result))

'''


# 두번째 생각
# 분자 계산과 분모 계산을 나누어서 생각
# 맞았다!!

'''
N, K = map(int, input().split())
mul_s = 1 # 분자
mul_m = 1 # 분모 

for i in range(N, N-K, -1):
    mul_s *= i

for i in range(K, 1, -1):
    mul_m *= i

result = mul_s / mul_m
print(int(result))

'''


# 세번째
# 파이썬 math 라이브러리를 통해 푸는 방법도 있다.
# 훨씬 코드가 짧아지고 한눈에 들어온다. 
# 이항 계수를 구하는 수학식 그대로를 팩토리얼을 통해 구현하면 된다. 
# n! / k!(n - k)!

from math import factorial

N, K = map(int, input().split())

result = factorial(N) / (factorial(K)*factorial(N-K))
print(int(result))