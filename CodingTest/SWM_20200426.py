import sys
sys.stdin=open("file.txt","rt")
'''
n = int(input())
a = list(map(int, input().split()))

lt = 0
rt = 1
largest = -2147000000

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += a[j]
        if tmp > largest:
            largest = tmp

print(largest)
'''
'''
n = int(input())

a = [list(list(map(int, input().split()))) for _ in range(n)]

b = list([0] * n)

for i in range(n):
    tmp = a[i][0]
    for j in range(n):
        if a[j][0] < tmp < a[j][1]:
            b[i] += 1

for i in range(n):
    print(b[i])
'''


n, m = map(int,input().split())

a = [list(list(map(int,input().split()))) for _  in range(n) ]

b= [list(list(map(int,input().split()))) for _  in range(m) ]

c = [[0]*(n+1)]*(n+1)

for i in range(m):
    if c[b[i][0]][b[i][1]] == 0:
        c[b[i][0]][b[i][1]]=1

print(c)

