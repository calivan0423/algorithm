import sys
sys.stdin = open("소수개수.txt","rt")

n= int(input())

'''
a=[0]*(n+1)
b=list()

for i in range(2,n+1):
    if a[i]==0:
        b.append(i)
        a[i]=1
        for j in range(0,int(n/i)):
            a[j*i]=1

print(len(b))
'''


a=[0]*(n+1)
cnt=0
for i in range(2,n+1):
    if a[i]==0:
        cnt+=1
    for j in range(i,n+1,i):
        a[j]=1

print(cnt)