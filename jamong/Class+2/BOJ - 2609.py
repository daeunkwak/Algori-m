"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 최대공약수와 최소공배수
description : 수학, 정수론, 유클리드 호제법

"""


# <최대공약수>
# 리스트 만들어서 num1과 num2를 
# 동시에 나누는 수를 집어넣는다.
# 그 리스트 안에서 가장 큰 수가 최대공약수

# <최소공배수>
# 최대공약수로 각각의 수를 나누고 나온 각각의 몫을 
# 최대공약수와 모두 곱하면 그 결과가 최소공배수 


# ver1

num1, num2 = map(int, input().split())
num_list = []
max = 1

for i in range(1, num1+1):
    if (num1 % i == 0) & (num2 % i == 0):
        num_list.append(i)
        if i > max:
            max = i

min = int(max * (num1/max) * (num2/max))

print(max)
print(min)




# 그런데 생각해보니까
# 어차피 최대공약수를 구할 때, 
# 당연히 리스트에 들어가는 수는 점점 커지니까 
# 리스트에 마지막으로 들어가는 수가 최대공약수가 된다.
# 그래서 if를 써서 max를 구하는 부분을 수정했다.


#ver 2

num1, num2 = map(int, input().split())
num_list = []

for i in range(1, num1+1):
    if (num1 % i == 0) & (num2 % i == 0):
        num_list.append(i)
        max = i

min = int(max * (num1/max) * (num2/max))

print(max)
print(min)