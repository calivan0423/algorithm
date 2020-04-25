import sys
#sys.stdin = open("격자판최대합.txt","rt")


n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

'''
value=0
for i in range(n):
    tmp=0
    for j in range(n):
        tmp=tmp+a[i][j]
    if tmp>value:
        value=tmp

for i in range(n):
    tmp=0
    for j in range(n):
        tmp=tmp+a[j][i]
    if tmp>value:
        value=tmp
tmp=0
for i in range(n):
    for j in range(n):
        if i==j:
            tmp+=a[i][j]
    if tmp > value:
        value = tmp

tmp=0
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            tmp+=a[i][j]
    if tmp > value:
        value = tmp

print(value)

'''

largest = -2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1 > largest:
        largest=sum1
    if sum2 > largest:
        largest=sum2

sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1 > largest:
    largest=sum1
if sum2 > largest:
    largest=sum2

print(largest)