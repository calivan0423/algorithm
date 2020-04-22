import sys
sys.stdin=open("회문문자열검사.txt","rt")

n=int(input())
'''
for i in range(n):
    st=str(input())
    st=st.lower()
    size=len(st)
    for j in range(size//2):
        if st[j]!= st[-1-j]:
            print("#%d NO"%(i+1))
            break
    else:
        print("#%d YES" %(i+1))
'''

for i in range(n):
    st=str(input())
    st=st.upper()
    if st==st[::-1]:
        print("#%d YES"%(i+1))
    else:
        print("#%d NO" % (i + 1))