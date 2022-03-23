import sys

lr = sys.stdin.readline

num = int(lr())

for _ in range(num):
    a = lr().split(' ')
    count = 0
    result = 0
    for i in range(1,len(a)):
        result += int(a[i])
    avr = result/int(a[0])
    for i in range(1, len(a)):
        if int(a[i])>avr:
            count += 1
    print('{:.3f}%'.format((count / int(a[0]) * 100)))