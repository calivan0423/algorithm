import sys
#sys.stdin= open("k 번째 큰 수.txt","rt")

n,k= map(int,input().split())

a= list(map(int,input().split()))

res=set() #중복제거 자료구조
for i in range(n):
    for j in range(i+1,n):
        for t in range(j+1,n):
            res.add(a[i]+a[j]+a[t])

res= list(res)
res.sort(reverse=True)
print(res[k-1])


