import sys
#sys.stdin = open("후위연산.txt","rt")

a = list(map(str,input()))

stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        tmp1=int(stack.pop())
        tmp2=int(stack.pop())
        if x=='+':
            stack.append(tmp2+tmp1)
        elif x=='-':
            stack.append(tmp2-tmp1)
        elif x=='*':
            stack.append(tmp2*tmp1)
        else :
            stack.append(tmp2/tmp1)

for x in stack:
    print(x,end='')