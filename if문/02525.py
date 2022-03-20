import sys

H, M = map(int, sys.stdin.readline().split(' '))
m1 = int(sys.stdin.readline())
t1 = m1//60
m0 = m1%60
if t1 >= 1:
    H += t1
    M += m0
    if M >= 60:
        H += 1
        M -= 60
        if H >= 24:
            H-=24
    elif H >= 24:
        H-=24
else:
    M += m0
    if M >=60:
        H+=1
        M-=60
        if H >=24:
            H-=24
print(H, M)