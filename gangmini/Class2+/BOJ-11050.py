'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 이항계수1
description : 수학, 구현, 조합론
'''

N, K = map(int, input().split())
p,s = 1,1
for i in range(K):
    p*=(N-i)
    s*=(K-i)
    #result *= (N-i)/(K-i)
print(int(p/s))
#분모 분자 나누셈을 마지막에 해주고 int형으로 바꾸어 준다