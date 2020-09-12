import sys
sys.stdin = open("음계.txt","rt")


def Discrimination_asc(list):
    type = True
    a = list[0]

    for i in range(1,len(list)):
         if list[i]==(a+1):
             a=list[i]
             continue
         else:
            type = False
            break

    return type


def Discrimination_des(list):
    type = True
    a = list[0]

    for i in range(1,len(list)):
        if list[i] == (a-1):
            a = list[i]
            continue
        else:
            type = False
            break

    return type



if __name__=="__main__":
    list = list(map(int,input().split()))
    a = Discrimination_asc(list)
    if a==1:
        print("ascending")
    else :
        b = Discrimination_des(list)
        if b==1:
            print("descending")
        else:
            print("mixed")
