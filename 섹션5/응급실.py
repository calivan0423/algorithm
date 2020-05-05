import sys
#sys.stdin = open("응급실.txt","rt")

n, m = map(int,input().split())
'''
a = list(map(int,input().split()))

b = []
for i,x in enumerate(a):
    b.append((i,x))
c = []
while b:

    x=b.pop(0)
    for j in range(len(b)):
        if b[j][1]>x[1]:
            b.append(x)
            break
    else:
        c.append(x)
for i in range(n):
    if c[i][0]==m:
        print(i+1)

'''
from _collections import deque

Q = [(pos,val) for pos, val in enumerate(list(map(int,input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt +=1
        if cur[0]==m:
            break

print(cnt)
