import  sys
#sys.stdin=open("두리스트합치기.txt","rt")



n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))

c=list()
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c.sort()

for x in c:
    print(x,end=' ')
'''

n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))

i=j=0
c=list()
while i<n1 and j<n2:
    if int(a[i]) <= int(b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

if i<n1:
    
    #for k in range(i,n1):
    #    c.append(a[k])
    
    c=c+a[i:]

if j<n2:
    
    #for w in range(j,n2):
    #    c.append(b[w])
    
    c=c+b[j:]

for x in c:
    print(x,end=' ')
'''
