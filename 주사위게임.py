import sys

sys.stdin = open("주사위게임.txt", "rt")

n = int(input())
res=0
for i in range(n):
    tmp=input().split()
    tmp.sort()
    a,b,c=map(int,tmp)
    if a==b and b==c:
        money=10000+a*1000
    elif a==b or a==c:
        money=1000 + a*100
    elif b==c:
        money = 1000 + b * 100
    else:
        money = 1000 + c * 100
    if money > res :
        res=money

print(res)

'''
def find_same(x):
    a = x[0]
    b = x[1]
    c = x[2]
    if a == b == c:
        return 3
    elif a == b != c:
        return 2
    elif a != b == c:
        return 2
    elif a == c != b:
        return 2
    else:
        return 1
    
def find_max(x):
    tmp = -1
    for i in range(3):
        if tmp < x[i]:
            tmp = x[i]
    return tmp

def find_twp(x):
    for i in range(0,3):
        if x.count(x[i]) == 2:
            return x[i]

b = list()
def result(x):
    d = find_same(x)
    if d == 3:
        return 10000 + a[0] * 1000
    elif d==2:
        tmp=find_twp(x)
        return 1000+tmp*100
    elif d==1:
        tmp=find_max(x)
        return tmp*100
    return 0

result_value=0
for i in range(n):
    a = list(map(int, input().split()))
    tmp=result(a)
    if tmp>result_value:
        result_value=tmp

print(result_value)
'''



