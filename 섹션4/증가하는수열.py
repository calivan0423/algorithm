import sys
#sys.stdin = open("증가하는수열.txt","rt")
from _collections import deque

'''
n = int(input())
a = list(map(int,input().split()))
a=deque(a)
tmp = 0
cnt = 0
res=''
for _ in range(n):
    if len(a)==1:
        if tmp < a[0]:
            res += 'L'
            cnt += 1
            break
    if tmp <a[0] and tmp <a[-1]:
        if a[0]<a[-1]:
            tmp =a[0]
            res+='L'
            cnt+=1
            a.popleft()
        else:
            tmp=a[-1]
            res+='R'
            cnt+=1
            a.pop()
    elif tmp <a[0]and tmp >a[-1]:
        tmp = a[0]
        res += 'L'
        cnt += 1
        a.popleft()
    elif tmp > a[0] and tmp <a[-1]:
        tmp = a[-1]
        res += 'R'
        cnt += 1
        a.pop()
print(cnt)
print(res)
'''

n = int(input())
a = list(map(int,input().split()))
lt=0
rt=n-1
last = 0
res=''
tmp=[]

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res+=tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1] =='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()

print(len(res))
print(res)

