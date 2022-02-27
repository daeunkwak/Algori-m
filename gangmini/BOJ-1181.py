'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 단어 정렬
description : 문자열, 정렬
'''

N = int(input())
s_dict={} #중복 불가능
s=''
s_list = [input()for _ in s]
for i in range(N):
    s_dict[s] = len(s)
s_dict = sorted(s_dict.items(), key=lambda x: x[1]) #문자열 길이로 정렬


