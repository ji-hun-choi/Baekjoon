import sys
lr = sys.stdin.readline

n = int(lr())

for _ in range(n):
    a = lr()
    count = 1
    result = 0
    for i in a:
        if i == 'O':
            result += count
            count += 1
        elif i == 'X':
            count = 1
    print(result)
