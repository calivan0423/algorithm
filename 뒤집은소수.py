import  sys
sys.stdin=open("뒤집은소수.txt","rt")

n=int(input())
a=list(map(int,input().split()))

def reverse(x):
    result = ''
    for i in str(x):
        result= i+ result
    return int(result)

def isPrime(x):
    val = True
    for i in range(2,x):
        if x%i==0:
            val=False
    return val
'''
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        t=t//10
    return res
    
def isPrime(x):
    if x==1:
        return True
    for i in range(2,x//2+1):
        if x%==0:
            return False
    else:
       return True
'''

for i in a:
    d = reverse(i)
    if isPrime(d):
        print(d,end=' ')
