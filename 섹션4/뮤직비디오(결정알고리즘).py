import sys
#sys.stdin = open("뮤직비디오(결정알고리즘).TXT","rt")


n , m = map(int,input().split())
a = list(map(int,input().split()))

maxx= max(a)

lt=1
rt = sum(a)

def Count(capacity):
    cnt = 1
    sum = 0
    for x in a:
        if sum+x > capacity :
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

count=0
result = 0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid) <= m:
        result = mid
        rt=mid-1
    else:
        lt=mid+1

print(result)