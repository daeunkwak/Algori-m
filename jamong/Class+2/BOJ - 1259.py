"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 팰린드롬수
description : 구현, 문자열

"""


while (True):
    num = str(input())
    if num == "0":
        break
    elif num == num[::-1]:
        print("yes")
    elif num != num[::-1]:
        print("no")


'''
<< 관련 파이썬 개념 >>

*파이썬 문자열 뒤집기, 거꾸로 출력하기 방법
 
1. 문자열 뒤집기 for 문
2. 문자열 뒤집기 reverse
3. 문자열 뒤집기 [::-1]

출처: https://blockdmask.tistory.com/581 [개발자 지망생]

'''