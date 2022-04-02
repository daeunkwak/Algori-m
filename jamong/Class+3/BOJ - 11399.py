"""
author : Cho Jayoung, 26006@naver.com
github : https://github.com/daeunkwak/Algori-m

title : ATM
description : 그리디 알고리즘, 정렬

"""


N = int(input())

Plist = list(map(int, input().split()))
Plist.sort() # 오름차순 정렬 
# 작은 숫자 앞으로 가면 시간 적게 걸림 

sum = 0

for i in range(N):  
    for j in range(i+1):
        sum += Plist[j]

print(sum)