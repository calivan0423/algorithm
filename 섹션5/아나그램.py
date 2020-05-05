import sys
sys.stdin =open("아나그램.txt","rt")
'''
p = dict()
str1=input()
str2=input()

for i in range(len(str1)):
    if str1[i] in p:
        p[str1[i]]+=1
    else:
        p[str1[i]]=1


for i in range(len(str2)):
    if str2[i] in p:
        p[str2[i]]-=1
    else:
        #print()
        print('NO')
# 위의 경우가 아닐 경우 아래 시행 안되야하는 문제 고쳐야함. flag값으로 조정?
for key,val in p.items():
    if val!=0:
       print('NO')
       break
else:
    print('YES')
'''

a=input()
b=input()
str1=dict()
str2=dict()

for x in a:
    str1[x]=str1.get(x,0)+1

for x in a:
    str2[x]=str2.get(x,0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print('NO')
            break
    else:
        print('NO')
        break
else:
    print('YSE')


