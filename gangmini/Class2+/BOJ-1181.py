'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 단어 정렬
description : 문자열, 정렬
'''

N = int(input())
s_list = list({input() for _ in range(N)})
s_list.sort() #사전순 정렬
s_list.sort(key=lambda x:len(x)) #길이순 정렬
for i in s_list:
    print(i)
