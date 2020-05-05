import sys
#sys.stdin = open ("쇠막대기.txt","rt")

s= input()

stack=[]
last =''
cnt = 0

'''
for x in s:
    if x == '(':
        stack.append(x)
    elif last=='(' and x ==')':
        stack.pop()
        cnt += len(stack)
    elif last==')' and x==')':
        cnt +=1
        stack.pop()
    last=x

print(cnt)
'''


for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
print(cnt)