import sys
#sys.stdin=open("점수계산.txt","rt")

n=int(input())
a=list(map(int,input().split()))

flag = True
pre_value = 0

count = 0
result= 0

for i in range(0,len(a)):
    if a[i]==1:
        if pre_value==1:
            count+=1
            result+=count
        else :
            count+=1
            result+=1
    elif a[i]==0:
        count=0
    pre_value=a[i]

print(result)
'''



sum=0
cnt=0

for x in a:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0

print(sum)
'''