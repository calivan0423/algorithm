

a ,b = map(int,input("숫자를 입력하세요.").split())

cnt = 0

for i in range(1,a+1):
    if a%1==0:
        cnt+=1
    if cnt==b:
        print(i)
        break
else:
    print(-1)




