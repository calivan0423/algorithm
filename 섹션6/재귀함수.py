import sys
#sys.stdin = open("재귀함수.txt","rt")


res = ''


def DFS(x):
    global  res
    if x ==0 :
        return
    else:
        tmp = str(x%2)
        res= tmp+ res
        DFS(x//2)




if __name__=="__main__":
    n=int(input())
    DFS(n)
    print(res)