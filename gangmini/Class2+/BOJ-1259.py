'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 팰린드롬수
description : 문자열, 구현
'''

num_list=[]
while(1):
    n = input()
    if(n =='0'):
        break
    num_list.append(n)
for s in num_list:
    start = 0
    end = len(s) - 1
    while(1):
        if(s[start]!=s[end]):
            print("no")
            break
        start +=1
        end -= 1
        if(start>=end):
            print("yes")
            break










