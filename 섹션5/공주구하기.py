import sys
sys.stdin = open("공주구하기.txt","rt")
'''
n, k = map(int, input().split())
a = list(range(1,n+1))

cnt = 0
res = 0
while a:
    cnt+=1
    if cnt != k :
        a.append(a.pop(0))
    else:
        res = a.pop(0)
        cnt=0

print(res)
'''
from _collections import deque

n, k = map(int,input().split())
dq=list(range(1,n+1))
dq=deque(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()