import sys

a = sys.stdin.readline().split(' ')
A=list()

for i in a:
    A.append(int(i))

if A[0]==A[1]==A[2]:
    print(10000+A[0]*1000)
elif A[0]==A[1] or A[0]==A[2]:
    print(1000+A[0]*100)
elif A[1]==A[2] and A[0]!=A[2]:
    print(1000+A[1]*100)
elif A[0]!=A[1]!=A[2]:
    print(max(A)*100)
