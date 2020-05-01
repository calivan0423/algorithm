import sys
sys.stdin = open("침몰하는타이타닉.txt","rt")

'''
n, m = map(int,input().split())
a = list(map(int,input().split()))

b= [0]*n
cnt = 0

a.sort()

for i in range(n):
    if b[i]==0:
        b[i]=1
        tmp= m-a[i]
        for j in range(n-1,0,-1):
            if tmp >= a[j] and b[j]==0:
                b[j]=1
                cnt+=1
                break
        else:
            b[i]=0

for i in range(n):
    if b[i]==0:
        b[i]=1
        cnt+=1

print(cnt)
'''

'''
n, limit = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
cnt=0
while p :
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1] >limit :
        p.pop()
        cnt+=1
    else :
        p.pop(0)
        p.pop()
        cnt+=1

print(cnt)
'''

from collections import deque

n, limit = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p=deque(p)
cnt = 0

while p :
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)