import sys
#sys.stdin = open("창고정리.txt","rt")

'''
L = int(input())
a = list(map(int,input().split()))
M = int(input())

highest =  -2174000000
lowest =  2174000000

for i in range(M):

    highest=max(a)
    a.remove(highest)
    a.append((highest-1))
    lowest= min(a)
    a.remove(lowest)
    a.append(lowest+1)

highest=max(a)
lowest=min(a)

print(highest-lowest)
'''

L = int(input())
a = list(map(int,input().split()))
m = int(input())

a.sort()

for _ in range(m):
    a[0]+=1
    a[L-1]-=1
    a.sort()

print(a[L-1]-a[0])