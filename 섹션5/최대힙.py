import sys
import heapq as hq
sys.stdin = open("최대힙.txt","r")

a = []
#최소힙에 부호를 바꾸어서 넣고....??? 다시 빼낼때는 - 붙여서...?

while True :
    n = int(input())
    if n== -1 :
        break
    if n== 0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)
