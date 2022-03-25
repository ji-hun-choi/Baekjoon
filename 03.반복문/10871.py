import sys
L=sys.stdin.readline
n, x = map(int,L().split(' '))
a = L().split(' ')
for i in range(n):
    if int(a[i]) < x :
        print(a[i], end=' ')