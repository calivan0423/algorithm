import sys
sys.stdin = open("교육과정설계.txt","rt")
from _collections import deque
essential = input()
n=int(input())
for i in range(n):
    need= deque( essential)
    plan = input()
    for x in plan:
        if x in need:
            if x!=need.popleft():
                print("#%d NO" %(i+1))
                break;
    else:
        if len(need)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))