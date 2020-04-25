import sys
#sys.stdin= open("랜선자르기.txt","rt")

def Count(len):
    cnt = 0
    for x in a:
        cnt += (x//len)
    return cnt


k , n = map(int,input().split())

a=[]
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    a.append(tmp)
    largest = max(largest,tmp)

lt=1
rt=largest


while lt <= rt :
    mid=(lt+rt)//2
    if Count(mid)>=n :
        res=mid
        lt= mid+1
    else:
        rt = mid-1

print(res)
