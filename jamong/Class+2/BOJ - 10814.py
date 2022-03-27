"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 나이순 정렬
description : 정렬

"""


'''
* 파이썬 람다 (lambda)
-> lambda 매개변수 : 표현식


ex) 두 수를 더하는 함수

>>> (lambda x,y: x + y)(10, 20)
30

'''


# 처음 생각했던 코드


N = int(input())

list = []

for i in range(N):
    age, name = map(str, input().split())
    list.append([int(age), i, name])  # i는 입력 순서 

list.sort()

for i in range(len(list)):
    print("{0} {1}".format(list[i][0], list[i][2]))




# 다른 분들의 코드를 보고 알게 된 방법

# lambda 사용

N = int(input())

list = []

for i in range(N):
    age, name = map(str, input().split())
    list.append([int(age), name])

list.sort(key=lambda x:x[0])
# arr[i][0]번째 위치 순으로 정렬
# sorted(arr, key=lambda x:x[0]) 와 같다.

for i in list:
    print(*i, sep=" ")  # *i는 리스트 형식을 없애준다.


# 출처: https://eunhee-programming.tistory.com/115