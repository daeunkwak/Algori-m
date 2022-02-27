"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : A+B - 4
description : 수학, 구현, 사칙연산

"""


#----<내가 작성한 오류 발생 코드>----
# import sys

# while (True):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)



# 오류 해결 코드 

import sys

while (True):
    try:
        a,b = map(int, sys.stdin.readline().split())
    except:
        break
    print(a+b)