import sys
#sys.stdin = open("역수열.txt","rt")

n = int(input())
a = list(map(int,input().split()))

seq = [0]*n

for i in range(1,n+1):
    for j in range(n):
        if a[i-1]==0 and seq[j]==0:
            seq[j]=i
            break
        elif seq[j]==0:
            a[i-1]-=1

for x in seq:
    print(x,end=' ')