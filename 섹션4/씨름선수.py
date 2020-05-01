import sys
#sys.stdin = open("씨름선수.txt","rt")

n = int(input())

palyer = []

for i in range(n):
    h, k = map(int, input().split())
    palyer.append((h,k))

palyer.sort(reverse=True)
largest = 0
cnt = 0

for x,y in palyer:
    if y > largest:
        largest = y
        cnt+=1

print(cnt)

