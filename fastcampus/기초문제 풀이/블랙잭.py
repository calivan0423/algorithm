import sys
sys.stdin = open("블랙잭.txt","rt")

n,m= map(int,input().split())
list= list(map(int,input().split()))

result = 0
length = len(list)

count  = 0

for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum=list[i]+list[j]+list[k]
            if sum<=m:
                result=(max(result,sum))

print(result)