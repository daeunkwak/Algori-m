'''
author : kyungmin Kim, keung903@naver.com
github : https://github.com/daeunkwak/Algori-m

title : 괄호
description : 자료 구조, 문자열, 스택
'''

from collections import deque
N = int(input())
statment = [list(map(str, input())) for _ in range(N)]
#print(statment)

# 조건1.(가 들어오면 넣는다
# 조건2. )가 들어오면 그 이전 원소가 (면 함께 pop한다. )전에 (가 없으면 NO!
# 조건3. 마지막까지 괄호가 남아있느면 NO!

for i in statment:
    stack = deque()
    for j in range(len(i)):
        if(i[j]==')' and len(stack)!=0): # 조건2_빈스택일 경우 성립X
            s = stack.pop()
            if (s != '('):
                stack.append(')')
            #print(stack)
        else:
            stack.append(i[j])
            #print(stack)

    # stack에 남은 요소가 있으면 NO!
    if(len(stack)==0):
        print('YES')
    else:
        print('NO')
