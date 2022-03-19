"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 소수 찾기
description : 수학, 정수론, 소수 판정, 에라토스테네스의 체

"""


# 첫번째

# 소수를 리스트에 넣어서 리스트 안의 요소의 개수를
# 세는 코드를 생각했다.

# 틀림.

num = int(input())
nums = list(map(int, input().split()))

num_list = []

for i in nums:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        num_list.append(i)

print(len(num_list))
    


# 두번째

# 소수의 개수를 담을 변수를 만들었다.

# 맞음.

num = int(input())
nums = list(map(int, input().split()))

num_cnt = 0

for i in nums:
    if i > 1:
        for j in range(2, i+1):
            if i % j == 0:
                if i == j:
                    num_cnt += 1
                break

print(num_cnt)