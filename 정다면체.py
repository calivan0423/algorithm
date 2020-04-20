import sys
sys.stdin=open("정다면체.txt","rt")

n, m = map(int,input().split())

'''
a=list()

for i in range(1,n+1):
    for j in range(1,m+1):
        a.append(i+j)

check = 0
value=list()
for i in a:
    tmp=0
    for j in range(0,len(a)):
        if a[j]==i:
            tmp+=1

    if tmp>check :
        check=tmp

for i in a:
    tmp = 0
    for j in range(0, len(a)):
        if a[j] == i:
            tmp += 1

    if tmp==check:
        if i not in value:
            value.append(i)

print(value)
'''


cnt=[0]*(n+m+3)
max=-2147000000

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i,end=' ')