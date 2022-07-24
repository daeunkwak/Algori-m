"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 영화감독 숌
description : 브루트포스 알고리즘

"""

N = int(input())
num_count = 0
num_six = 666

while True:
    if '666' in str(num_six):
        num_count += 1

    if num_count == N:
        print(num_six) # N번째 영화의 제목에 들어간 숫자
        break

    num_six += 1