import sys
import itertools as it
sys.stdin = open("수들의조합.txt","rt")

if __name__=="__main__":
    n, k = map(int,input().split())
    a=list(map(int,input().split()))
    m = int(input())
    cnt = 0
    for tmp in it.combinations(a,k):
        if sum(tmp)%m==0:
            cnt+=1
print(cnt)


'''
def DFS(L,s,sum):
    global cnt
    if L == k:
        if sum%m==0 :
            cnt= cnt + 1
    else :
        for i in range(s,n):
            DFS(L+1,i+1,sum+a[i])


if __name__=="__main__":
    n, k = map(int,input().split())
    a=list(map(int,input().split()))
    res=[0]*(n+1)
    m = int(input())
    cnt = 0
    DFS(0,0,0)
    print(cnt)
'''