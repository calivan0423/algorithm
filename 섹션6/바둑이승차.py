import sys
#sys.stdin = open("바둑이승차.txt","rt")


def DFS(L,sum,totsum):
    global result
    if sum+(total-totsum) < result:
        return
    if sum >c :
        return
    if L == n :
        if sum > result:
            result =sum
    else:
        DFS(L+1,sum+a[L],totsum+a[L])
        DFS(L+1,sum,totsum+a[L])



if __name__=="__main__":
    c , n= map(int,input().split())
    a = [0]*n
    result = -2147000000
    for i in range(n):
        a[i]=int(input())
    total = sum(a)
    DFS(0,0,0)
    print(result)