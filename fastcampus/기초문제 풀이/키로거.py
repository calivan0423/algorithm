import sys
sys.stdin = open("키로거.txt","rt")

import queue

test_case = int(input())


for i in range(test_case):
    left = []
    right = []
    data=input()
    for i in data:
        if i=='-':
            if left:
                left.pop()
        elif i=='<':
            if left:
                right.append(left.pop())
        elif i=='>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))

