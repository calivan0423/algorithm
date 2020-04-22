import sys
#sys.stdin= open("자릿수합.txt","rt")

n=int(input())
a=list(map(int,input().split()))

def digit_sum(x):
    sum=0
    while x>0:
        sum+= x%10
        x=x//10
    return sum


result=-1
result_index=0
for i in range(0,n):
    tmp=digit_sum(a[i])
    if result < tmp:
        result=tmp
        result_index=i

print(a[result_index])

'''
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

result=-1
for x in a:
    tmp=digit_sum(x)
    if tmp>result:
        result=tmp
        res=x
print(res)
'''