"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 괄호
description : 자료 구조, 문자열, 스택

"""


# 처음 생각한 코드
# 예제를 입력하고 결과를 보다가 틀렸음을 알았다.
# 개수만 일치하는지 확인을 하게 되면 
# )( -> 이런 경우도 올바르다고 하게 된다.

T = int(input())

for i in range(T):
    VPN = input()
    VPN_list = list(VPN)
    left_count = 0
    right_count = 0

    for j in VPN_list:
        if j == "(":
            left_count += 1
        elif j == ")":
            right_count += 1

    if left_count == right_count:
        print("YES")
    else:
        print("NO")


# 수정한 코드
# 여는 괄호보다 닫는 괄호가 더 많아지는 순간
# 종료하는 코드

T = int(input())

for i in range(T):
    VPN = input()
    VPN_list = list(VPN)
    sum = 0

    for j in VPN_list:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1

        if sum < 0:
            print("NO")
            break

    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")