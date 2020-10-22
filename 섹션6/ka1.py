import sys
sys.stdin=open("ka1.txt","rt")

import re

def solution(new_id):
    id=new_id.lower()
    #1단계
    id= re.sub('[^a-z0-9_.-]+','',id)
    id=list(id)
    #2단계
    id2=[]
    for i in range(0,len(id)):
        if id[i-1]=='.':
            if id[i-1]!=id[i]:
                id2+=id[i]
        else:
            id2+=id[i]
    #3단계
    if len(id2)>0:
        if id2[0]=='.' :
            id2.pop(0)
    if len(id2) > 0:
        if id2[-1]=='.':
            id2.pop()

    #4단계
    if len(id2)==0:
        id2.append('a')

    #5단계
    if len(id2)>=16:
        id2=id2[:15]
        if id2[-1]=='.':
            id2.pop()
    #6단계

    while len(id2)<3:
        id2.append(id2[-1])
    #7단계
    answer=''
    for x in id2:
        answer+=x
    #print(answer)
    return answer


if __name__=="__main__":
    id=input()
    solution(id)
