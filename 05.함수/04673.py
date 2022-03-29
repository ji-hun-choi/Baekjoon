def d(n):
    if n == 10000:
        a = n // 10000
        nextNum = n + a
    elif n >= 1000:
        a = n // 1000
        b = (n % 1000) // 100
        c = ((n % 1000) % 100) // 10
        d = ((n % 1000) % 100) % 10
        nextNum = n + a + b + c + d
    elif n >= 100:

        a = n // 100

        b = (n % 100) // 10

        c = (n % 100) % 10

        nextNum = n + a + b + c
    elif n < 100:

        a = n // 10

        b = n % 10

        nextNum = n + a + b
    if nextNum <= 10000:
        Init_list.append(nextNum)


Init_list = []

for i in range(1, 10001):
    d(i)

Init_list.sort()

Init_list = set(Init_list)

# print(Init_list)


for i in range(1, 10001):
    if i in Init_list:
        continue
    else:
        print(i)