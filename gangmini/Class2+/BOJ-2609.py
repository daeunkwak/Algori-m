'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 최대공약수 최소공배수
description : 수학, 정수, 유클리드 호제법 '''


def max_f(a,b):
    if(a % b == 0):
        return b
    if(a % b == 1):
        return 1
    return max_f(b,a%b)

n,m = map(int,input().split())
#n%m 연산을 위해 n<m인 경우 바꿔줌
if(n<m):
    tmp = n
    n = m
    m =tmp
mmax = max_f(n,m)
print(mmax) #최대공약수
mmin = mmax*(n//mmax)*(m//mmax)
print(mmin) #최소공배수 ##최대공약수*(최대공약수로 각 수 나눈값)

##유클리드 호제법
#큰 수를 작은 수로 나눠서 나머지가 나오면 이번엔 작은 수를 나머지로 나눈다.
#나눠 떨어질 때까지 반복
