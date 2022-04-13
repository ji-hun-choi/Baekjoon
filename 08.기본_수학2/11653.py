a = int(input())
flag = True
while flag:
    for i in range(2, a+1):
        if a % i == 0:
            a = a//i
            print(i)
            break
    if a == 1:
        flag = False