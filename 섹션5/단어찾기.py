import sys
#sys.stdin = open("단어찾기.txt","rt")
n=int(input())
p=dict()

for i in range(n):
    word=input()
    p[word]=1

for i in range(n-1):
    use_word=input()
    p[use_word]=0

for key,val in p.items():
    if val!=0:
        print(key)