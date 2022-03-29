import sys

rl = sys.stdin.readline

num = int(rl())

for i in range(num):
    a = rl().split(' ')
    for j in a[1]:
        if '\n' not in j:
            print(j*int(a[0]), end='')
    print()
