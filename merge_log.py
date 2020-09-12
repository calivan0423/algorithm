import os

# 로그 파일이 모두 한 폴더 내에 존재해야한다.

directory = "logs/"  #로그파일들이 들어 있는 하위 폴더
outfile_name_M="merge_log_M.txt" #통합 M 로그 파일
outfile_name_S="merge_log_S.txt" #통합 S 로그 파일

#개수 파악
a=0
b=0

out_file_M = open(outfile_name_M,'w')
out_file_S = open(outfile_name_S,'w')

files = os.listdir(directory)
for filename in files:
    #로그 파일을 통합하는 과정 수행
    file = open(directory + filename)
    if filename.endswith('M.txt'):
        #M의 로그 파일일 경우
        for line in file:
            out_file_M.write(line)
        out_file_M.write("\n")
        a+=1
    if filename.endswith('S.txt'):
        #S의 로그 파일일 경우
        for line in file:
            out_file_S.write(line)
        out_file_S.write("\n")
        b+=1
    file.close()
    print(a, b)
out_file_M.close()
out_file_S.close()



