import time

def extraction(file):
    List = []
    with open(file) as f:
        for line in f:
            if(len(line.split('peer='))==1):
                continue
            List.append(line.split('peer=')[1].split('\n')[0])
    List=list(set(List))
    List.sort()
    return List

def compare(List_m, List_s):
    # 양쪽 로그의 source address를 비교
    List_re = []
    for i in range(len(List_m)):
        tmp = str(List_m[i])
        if tmp not in List_s:
            List_re.append(tmp)
    return List_re


def file_out(List1,List2):
    # 최종 결과 파일 생성
    f = open('Result_M_to_S.txt', mode='wt', encoding='utf-8')
    f.write('DHCP Main서버 로그에만 찍힌 OLT 장비 ip주소 목록\n\n\n')
    for i in List1:
        f.write(i + '\n')
    f.close()
    f = open('Result_S_to_M.txt', mode='wt', encoding='utf-8')
    f.write('DHCP Slave서버 로그에만 찍힌 OLT 장비 ip주소 목록\n\n\n')
    for i in List2:
        f.write(i + '\n')
    f.close()


if __name__ == "__main__":
    # extract test
    '''
    file='SLSDM3-M_DISCOVER.txt.'
    List_M = []
    f = open(file,'r')
    line_num_M=1
    line_M=list(map(str,f.readline().split()))
    tmp=str(line_M[-1])
    List_M.append(tmp)
    while line_M:
        line_M = list(map(str, f.readline().split()))
        if len(line_M)==0:
            break
        tmp = str(line_M[-1])
        List_M.append(tmp)
        line_num_M+=1
    f.close()
    List_M = list(set(List_M))
    List_M.sort()
    length_M = len(List_M)


    for i in range(length_M):
        print(List_M[i])
    print(length_M)


    List_S = []
    f = open('SLSDM3-S_DISCOVER.txt.', 'r')
    line_num_S = 1
    line_S = list(map(str, f.readline().split()))
    tmp = str(line_S[-1])
    List_S.append(tmp)
    while line_S:
        line_S = list(map(str, f.readline().split()))
        if len(line_S) == 0:
            break
        tmp = str(line_S[-1])
        List_S.append(tmp)
        line_num_S += 1
    f.close()
    List_S = list(set(List_S))
    List_S.sort()
    length_S = len(List_S)


    for i in range(length_S):
        print(List_S[i])
    print(length_S)
    '''
    start = time.time()  # 시작 시간 저장
    List_M = extraction('SLSDM3-M_DISCOVER.txt.')
    List_S = extraction('SLSDM3-S_DISCOVER.txt.')
    List_result = compare(List_M, List_S)
    List_result2 = compare(List_S, List_M)

    file_out(List_result,List_result2)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

    # file out test
    '''
    f = open('result_result.txt',mode='wt',encoding='utf-8')
    for i in range(length_result):
        f.write(List_result[i])
        f.write('\n')
    f.close()
    '''

    # result print test
    '''
    for i in range(len(List_result)):
        print(List_result[i])
    print(length_result,length_M,length_S,length_M-length_S)
    '''