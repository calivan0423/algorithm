import sys
import itertools as it
sys.stdin = open("순열추측하기.txt","rt")

n,f=map(int,input().split())
p=[0]*n
b=[1]*n
ch = [0]*(n+1)
for i in range(1,n):
    b[i]=(b[i-1]*(n-i))//(i)
a=list(range(1,n+1))
for tmp in it.permutations(a):
    sum=0
    for L,x in enumerate(tmp):
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x,end=' ')
        break


'''
def DFS(L,sum):
    if L==n and sum==f:
        for x in p:
            print(x,end='')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1,sum+(p[L]*b[L]))
                ch[i]=0


if __name__=="__main__":
    n,f=map(int,input().split())
    p=[0]*n
    b=[1]*n
    ch = [0]*(n+1)
    for i in range(1,n):
        b[i]=(b[i-1]*(n-i))//(i)
    DFS(0,0)

'''