'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 나이순 정렬
description : 정렬
'''


N = int(input())
mem = list(input().split() for _ in range(N))
print(mem)
#mem.sort(key=lambda x:int(x[0])) #value값->age을 기준으로 정렬
mem = sorted(mem,key=lambda x:int(x[0])) #int형으로 바꿔줘 숫자를 기준으로 정렬해야 정답
for j in mem:
    print(j[0],j[1])

#변수명.sort() vs sorted() 함수 차이



