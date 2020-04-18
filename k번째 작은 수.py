import sys
sys.stdin=open("k번째 작은 수.txt","rt")


T= int(input("숫자를 입력하세요\n"))
'''
for t in range(T):
    que = []
    n, s, e, k = map(int, input("숫자를 입려갛세요").split())
    a= list(map(int,input().split()))

    for i in range(s,e+1):
        que.append(a[i-1])
    que.sort()
    print("#%d %d" %(t,que[k-1]))
    que.clear()
'''

for t in range(T):
    n, s, e, k = map(int, input("숫자를 입려갛세요").split())
    a= list(map(int,input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
