'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 소수 찾기
description : 수학,정수론,소수 판정,에라토스테네스의 체
'''

#에라토스테네스의 체 : 2부터 시작하여 자기 자신을 넘지 않는 선에서 배수들을 지워나감 #자기 자신도 지우면 X


import math

def isPrime(x):
    if(x==1): # 1은 소수가 아님
        return False
    for i in range(int(math.sqrt(x))):
        if(i==0):
            continue
        if(x%(i+1)==0):
            return False
    return True


N = int(input())
num_list = list(map(int,input().split()))

count=0
for i in num_list:
    if(isPrime(i) == True):
        count = count + 1

print(count)


