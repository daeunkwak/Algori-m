"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 직각삼각형
description : 수학, 기하학, 피타고라스 정리 

"""

# 우선은 a, b, c 중에서 어떤 것이 가장
# 기 변이 될 지 모르니까 모든 경우를 다 비교하도록 했다.

while(True):
    a, b, c = map(int, input().split())
    if a == 0 | b == 0| c == 0:
        break
    elif a*a + b*b == c*c:
        print("right")
    elif b*b + c*c == a*a:
        print("right")
    elif a*a + c*c == b*b:
        print("right")
    else:
        print("wrong")


# 조금만 더 생각해보면 모든 경우를 다 셀 필요없이
# 가장 긴 변만 정해주고 나머지를 제곱해서 더하는 
# 코드를 짤 수 있을 것 같다. 