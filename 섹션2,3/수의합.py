import sys
sys.stdin=open("수의합.txt","rt")


n, m= map(int,input().split())
a=list(map(int,input().split()))

'''
value=0
result=0
for i in range(n):
    for j in range(i,n):
       value+=a[j]

       if value==m:
           result+=1
    value=0

print(result)

#시간복잡도가 N^2이라 높은 편
'''


lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        else:
            break
    elif tot == m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)

