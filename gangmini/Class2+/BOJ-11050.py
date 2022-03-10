'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 이항계수1
description : 수학, 구현, 조합론
'''

N,K = map(int,input.split())
result = 0
for i in range(K):
    result *= (N-i)/(K-i)
print(result)