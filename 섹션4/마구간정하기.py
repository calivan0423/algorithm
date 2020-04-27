import sys
#sys.stdin = open("마구간정하기.TXT","rt")

n , c = map(int, input().split())
Line = []

for i in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()

def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1,n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

lt=1
rt=Line[n-1]
res = 0
while lt <= rt:
    mid=(lt+rt)//2
    if Count(mid) >= c:
        res=mid
        lt= mid+1
    else:
        rt=mid-1

print(res)