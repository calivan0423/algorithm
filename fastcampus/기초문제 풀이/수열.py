import sys
sys.stdin = open("수열.txt","rt")



if __name__=="__main__":

    n = int(input())
    list = []
    b = 1
    result = []


    for i in range(n):
        k = int(input())
        while b<=k:
            list.append(b)
            b+=1
            result.append('+')
        if list[-1]==k:
            list.pop()
            result.append('-')
        else:
            print("NO")
            exit(0)

    print('\n'.join(result))

