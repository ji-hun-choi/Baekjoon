import sys
L = sys.stdin.readline
n = int(L())
for i in range(n):
    a, b = map(int, L().split(' '))
    print(a+b)