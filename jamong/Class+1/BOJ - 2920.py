"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 음계
description : 구현

"""


scale = list(map(int, input().split()))

if scale == sorted(scale): #오름차순 정렬
    print("ascending")

elif scale == sorted(scale, reverse=True): #내림차순 정렬 
    print("descending")

else:
    print("mixed")