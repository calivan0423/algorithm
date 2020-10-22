

def solution(info, query):
    answer=[]

    for x in query:
        tmp = list(x.split(' '))
        cnt = 0
        q = tmp[:-1]
        q = set(q)
        q.remove('and')
        num = tmp.count('-')
        for y in info:
            tmp2 = list(y.split(' '))
            if int(tmp[-1]) <= int(tmp2[-1]):
                w = tmp2[:-1]
                w = set(w)
                k = w - q
                if len(k) == num:
                    cnt += 1
        answer.append(cnt)

    '''
    for x in info:
        tmp_info.append(x.split())
    for x in query:
        tmp = list(x.split(' '))
        tmp.remove('and')
        tmp.remove('and')
        tmp.remove('and')
        tmp_query.append(tmp)

    for x in tmp_query:
        cnt=0
        q=x[:-1]
        q=set(q)
        num = x.count('-')

        for y in tmp_info:
            w=y[:-1]
            w=set(w)
            k=w-q
            if len(k)==num:
                if int(x[-1])<=int(y[-1]):
                    cnt+=1
        answer.append(cnt)



   
    for x in tmp_info:
        for y in range(len(tmp_query)):
            if (x[0]==tmp_query[y][0]) or tmp_query[y][0]=='-':
                if (x[1] == tmp_query[y][1]) or tmp_query[y][1] == '-':
                    if (x[2] == tmp_query[y][2]) or tmp_query[y][2] == '-':
                        if (x[3] == tmp_query[y][3]) or tmp_query[y][3] == '-':
                            if (int(x[4]) >= int(tmp_query[y][4])) or int(tmp_query[y][4]) == '-':
                                answer[y]+=1

    
    for x in range(len(tmp_query)):
        for y in tmp_info:
            if (y[0]==tmp_query[x][0]) or tmp_query[x][0]=='-':
                if (y[1]==tmp_query[x][1]) or tmp_query[x][1]=='-':
                    if (y[2] == tmp_query[x][2]) or tmp_query[x][2] == '-':
                        if (y[3] == tmp_query[x][3]) or tmp_query[x][3] == '-':
                            if (int(y[4]) >= int(tmp_query[x][4])) or int(tmp_query[x][4])=='-':
                                answer[x]+=1
    '''


    return answer

if __name__=="__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query =  ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

    answer = solution(info,query)
    print(answer)


