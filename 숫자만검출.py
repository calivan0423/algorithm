import sys
sys.stdin=open("숫자만검출.txt","rt")

'''
st=str(input())
size=int(len(st))
result = ''

for i in range (size):
    if 48<=ord(st[i])<=75:
        result+=st[i]
        
result=int(result)
value =0

for i in range(1,result+1):
    if result%i==0:
        value+=1

print(result)
print(value)
'''

s=input()
res=0

for x in s:
    if x.isdecimal():
        res=res*10+int(x)

print(res)
cnt=0

for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)