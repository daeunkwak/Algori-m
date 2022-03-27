'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 소수 찾기
description : 수학,정수론,소수 판정,에라토스테네스의 체
'''

#에라토스테네스의 체 : 2부터 시작하여 자기 자신을 넘지 않는 선에서 배수들을 지워나감 #자기 자신도 지우면 X

N = int(input())
num_list = list(map(int,input().split()))
new_list=[]
for i in num_list:
    if(i==1):
        continue
    finding_num=[]
    #찾고자 하는 수의 배열 초기화
    for j in range(i):
        finding_num.append(j+1)

    for d in range(2,i):
        count = 1
        while(1):
            if (d * count >= i):
                break
            finding_num.remove(d * count) #이미 지운게 여러번 중복삭제 되는 문제
            count += 1
            print(finding_num)


    if(len(finding_num)==2):
        new_list.append(i)

print(len(new_list))
