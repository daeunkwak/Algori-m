'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 블랙잭
description : 브루트포스 알고리즘 '''

N, M = map(int, input().split())
card = list(map(int, input().split()))

max = 0
end = len(card)
for i in range(0,end-2):
    for j in range(i+1,end-1):
        for k in range(j+1,end):
            sum = card[i]+card[j]+card[k]
            if(sum == M):
                print(sum)
                exit(0)
            if(max<sum<M):
                max = sum
print(max)
