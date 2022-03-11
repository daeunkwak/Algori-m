'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 최대공약수 최소공배수
description : 수학, 정수, 유클리드 호제법 '''


def max_(a,b):
    if(a%b==0):
        return b
    max_(b,a%b)

n,m = map(int,input().split())
if(n<m):
    tmp = n
    n = m
    m =tmp
max_div = max_(n,m)
min_mul = max_div*(n/max_div)*(m/max_div)
print(max_div) #최대공약수
print(min_mul) #최소공배수 ##최대공약수*(최대공약수로 각 수 나눈값)

##유클리드 호제법
#큰 수를 작은 수로 나눠서 나머지가 나오면 이번엔 작은 수를 나머지로 나눈다.
#나눠 떨어질 때까지 반복