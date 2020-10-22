import sys
sys.stdin = open("ka2.txt","rt")

from itertools import combinations

if __name__=="__main__":

    orders =["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course = [2,3,5]
    answer = []

    for n in course:
        tmp = {}
        for x in orders:
            x = list(x)
            x_com = list(combinations(x, n))
            for j in x_com:
                cnt = 0
                j = set(j)
                for q in orders:
                    q=list(q)
                    q=set(q)
                    w=j-q
                    if len(w)==0:
                        cnt+=1
                if cnt>1:
                    j=list(j)
                    j.sort()
                    t="".join(j)
                    if t not in tmp:
                        tmp[t]=0
                    else:
                        tmp[t]+=1
        menu=sorted(tmp.items(),key=lambda  x:x[1],reverse=True)
        if(len(menu)!=0):
            k=menu[0][1]
            for i in menu:
                if i[1] == k:
                    if i[0] not in answer:
                        answer.append(i[0])
                else:
                    break
    answer.sort()
    print(answer)

    '''
    for x in course:
        for k in orders:
            cnt = 0
            if len(k)==x:
                k=list(k)
                q=set(k)
                for j in orders:
                    j=list(j)
                    j=set(j)
                    if len(q-j)==0:
                        cnt+=1
            if cnt>1:
                k=list(k)
                k="".join(k)
                if k not in answer:
                    answer.append(k)
    '''


